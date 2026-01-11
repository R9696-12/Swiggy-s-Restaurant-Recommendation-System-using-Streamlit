# 🍽️ Swiggy’s Restaurant Recommendation System using Streamlit

## 📌 Project Overview
This project implements a **restaurant recommendation system** using Swiggy restaurant data.  
The system recommends restaurants based on user preferences such as **city, cuisine, rating, and cost**.  
A **Streamlit web application** is built to provide an interactive and user-friendly interface.

---

## 🧠 Domain
Recommendation Systems and Data Analytics

---

## 🛠️ Skills Gained
- Data Preprocessing  
- One-Hot Encoding  
- Clustering / Similarity-Based Recommendation  
- Streamlit Application Development  
- Python Programming  

---

## 🎯 Problem Statement
The objective is to build a recommendation system using restaurant data provided in a CSV file.  
The system suggests restaurants based on user input features such as **city, rating, cost, and cuisine preferences** using clustering or similarity-based techniques.

---

## 📂 Dataset Description
The dataset contains the following columns:

### Feature Types
- **Categorical:** name, city, cuisine  
- **Numerical:** rating, rating_count, cost  

---

## 🚀 Project Approach

### 1️⃣ Data Understanding & Cleaning
- Removed duplicate records  
- Handled missing values  
- Saved the cleaned dataset as:
  - `cleaned_data.csv`

---

### 2️⃣ Data Preprocessing
- Applied **One-Hot Encoding** to categorical features:
  - `city`
  - `cuisine`
- Ensured all features are numerical  
- Maintained index consistency between datasets  
- Generated:
  - `encoded_data.csv`
  - `encoder.pkl`

---

### 3️⃣ Recommendation Methodology
- Used **Clustering (K-Means)** or **Cosine Similarity**  
- Performed similarity calculations on encoded data  
- Mapped recommendation results back to the cleaned dataset  

---

### 4️⃣ Streamlit Application
The application includes:
- **User Input:** City, cuisine, rating, cost  
- **Recommendation Engine:** Processes user inputs and computes similarity  
- **Output:** Displays recommended restaurants from cleaned data  

---

## 📊 Results

### Data Outputs
- **cleaned_data.csv**  
  - Cleaned dataset with missing values and duplicates removed  

- **encoded_data.csv**  
  - Fully numerical dataset after One-Hot Encoding  

- **encoder.pkl**  
  - Serialized encoder for Streamlit application  

---

### Recommendation System
- Similarity or clustering-based recommendations  
- Accurate mapping between encoded and original datasets  

---

### Streamlit Application
- Interactive and user-friendly interface  
- Real-time restaurant recommendations  

---

## 🏢 Business Use Cases
1. Personalized restaurant recommendations  
2. Improved customer experience  
3. Market insights and preference analysis  
4. Operational efficiency for food businesses  

---

## 🧪 Technologies Used
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit  


## ▶️ How to Run the Project
- streamlit run app.py




