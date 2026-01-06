import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MultiLabelBinarizer

# -----------------------------
# Load Dataset
# -----------------------------
df_cleaned = pd.read_csv(r"C:\Swiggy restaurant\cleaned_data.csv")
restaurants = df_cleaned.copy()

# -----------------------------
# Build Encoders On The Fly (no external pickle needed)
# -----------------------------

def _split_cuisines(cuisine_str: str):
    if not isinstance(cuisine_str, str):
        return []
    parts = []
    for chunk in cuisine_str.replace("/", ",").replace("|", ",").split(","):
        t = chunk.strip()
        if t:
            parts.append(t)
    return parts

# Identify numeric columns present
possible_num_cols = ["rating", "rating_count", "cost"]
num_cols = [c for c in possible_num_cols if c in restaurants.columns]

# Prepare numeric matrix
num_mat = restaurants[num_cols].to_numpy(dtype=float) if num_cols else np.empty((len(restaurants), 0))
scaler = StandardScaler()
num_scaled = scaler.fit_transform(num_mat) if num_cols else num_mat

# City one-hot
city_vals = restaurants["city"].astype(str).values.reshape(-1, 1)
city_encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
city_ohe = city_encoder.fit_transform(city_vals)

# Cuisine multi-label binarization
cuisine_lists = restaurants["cuisine"].apply(_split_cuisines)
cuisine_encoder = MultiLabelBinarizer()
cuisine_ohe = cuisine_encoder.fit_transform(cuisine_lists)

# Concatenate to get encoded features for all restaurants
encoded_features = np.concatenate([num_scaled, city_ohe, cuisine_ohe], axis=1).astype(float)

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Restaurant Recommender", layout="wide")
st.title("🍽️ Restaurant Recommendation System")

st.sidebar.header("User Preferences")

selected_city = st.sidebar.selectbox(
    "City",
    sorted(restaurants['city'].unique())
)

selected_cuisine = st.sidebar.selectbox(
    "Cuisine",
    sorted(restaurants['cuisine'].unique())
)

min_rating = st.sidebar.slider(
    "Minimum Rating",
    float(restaurants['rating'].min()),
    float(restaurants['rating'].max()),
    float(restaurants['rating'].median())
)

max_budget = st.sidebar.slider(
    "Maximum Budget (₹)",
    float(restaurants['cost'].min()),
    float(restaurants['cost'].max()),
    float(restaurants['cost'].median())
)

# -----------------------------
# User Input Processing
# -----------------------------
# Build numeric features
num_vals = []
for col in num_cols:
    if col == "rating":
        num_vals.append(min_rating)
    elif col == "rating_count":
        num_vals.append(0.0)  # neutral rating count
    elif col == "cost":
        num_vals.append(max_budget)
    else:
        num_vals.append(0.0)

num_scaled = scaler.transform([num_vals]) if num_vals else np.empty((1, 0))

# Encode city
city_arr = np.array([[str(selected_city)]])
city_ohe = city_encoder.transform(city_arr)

# Encode cuisine (handle multi-label)
# Split selected cuisine if it contains multiple cuisines
cuisine_list = [c.strip() for c in selected_cuisine.replace('/', ',').split(',')]
cuisine_ohe = cuisine_encoder.transform([cuisine_list])

# Concatenate all features
user_scaled = np.concatenate([num_scaled, city_ohe, cuisine_ohe], axis=1).astype(float)

# -----------------------------
# Similarity Calculation
# -----------------------------
similarity_scores = cosine_similarity(
    user_scaled,
    encoded_features
).flatten()

restaurants['similarity_score'] = similarity_scores

# -----------------------------
# Apply Filters
# -----------------------------
filtered_restaurants = restaurants[
    (restaurants['rating'] >= min_rating) &
    (restaurants['cost'] <= max_budget) &
    (restaurants['city'].astype(str) == str(selected_city))
]

# -----------------------------
# Final Recommendations
# -----------------------------
top_recommendations = (
    filtered_restaurants
    .sort_values(by='similarity_score', ascending=False)
    .head(5)
)

# -----------------------------
# Display Results
# -----------------------------
st.subheader("🔝 Recommended Restaurants")

if len(top_recommendations) > 0:
    st.dataframe(
        top_recommendations[
            ['name', 'city', 'cuisine', 'rating', 'cost', 'address']
        ],
        use_container_width=True
    )
else:
    st.warning("No restaurants match your criteria. Try adjusting the filters.")



st.markdown("### 📊 Summary")
st.markdown(f"""
- Total restaurants analyzed: **{len(restaurants)}**
- Restaurants matching filters: **{len(filtered_restaurants)}**
- Recommendations generated: **{len(top_recommendations)}**
""")
# Generate Summary Report
st.write("### Recommendation Methodology:")
st.write("- Used **K-Means Clustering** for grouping restaurants")
st.write("- Applied **Cosine Similarity** for personalized recommendations")

st.write("### Key Results:")
st.write(f"- Processed `{len(restaurants)}` restaurants")
st.write(f"- Found `{top_recommendations.shape[0]}` matching recommendations")