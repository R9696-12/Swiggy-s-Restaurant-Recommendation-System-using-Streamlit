# 🍽️ Swiggy Restaurant Recommendation System using Streamlit

## 📌 Project Overview
This project implements a **restaurant recommendation system** using Swiggy restaurant data.  
It recommends restaurants based on user preferences such as **city, cuisine, rating, and budget** using **machine learning techniques** and displays results through a **Streamlit web application**.

---

## 🎯 Problem Statement
To build a recommendation system that analyzes restaurant data from a CSV file and provides personalized restaurant suggestions using **clustering and similarity-based approaches**.

---

## 🧠 Domain
Recommendation Systems & Data Analytics

---

## 🛠️ Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- One-Hot Encoding
- K-Means Clustering
- Cosine Similarity
- Streamlit
  
### Feature Types:
- **Categorical:** city, cuisine
- **Numerical:** rating, rating_count, cost

---

## 🔄 Project Workflow

### 1️⃣ Data Cleaning
- Removed duplicate records
- Converted cost and rating to numerical format
- Handled missing values using median imputation
- Dropped unnecessary columns
- Saved cleaned data as `cleaned_data.csv`

---

### 2️⃣ Data Encoding
- Applied **One-Hot Encoding** to `city` and `cuisine`
- Ensured all features are numerical
- Saved:
  - `encoded_data.csv`
  - `encoder.pkl`

---

### 3️⃣ Clustering
- Standardized numerical features
- Applied **K-Means clustering**
- Assigned cluster labels to restaurants
- Saved clustered data as `clustered_data.csv`

---

### 4️⃣ Recommendation System
- Used **Cosine Similarity** to find similar restaurants
- Compared user preferences with restaurant feature vectors
- Returned top N similar restaurants

---

### 5️⃣ Streamlit Application
- User inputs:
  - City
  - Cuisine
  - Minimum rating
  - Budget
- Displays:
  - Recommended restaurants with details
  - streamlit run app.py


