# 🛍️ Customer Conversion Analysis for Online Shopping Using Clickstream Data

An end-to-end data analytics and machine learning project designed to analyze e-commerce clickstream data and enhance customer conversions, forecast revenue, and segment customers. This project was developed as part of the **Naan Mudhalvan** skill development initiative under the **Data Analytics in Process Industries** course.

---

## 🏫 Academic Information

**Institution**: 1105 - Gojan School of Business and Technology (GSBT)  
**Program**: Naan Mudhalvan  
**Course Name**: Data Analytics in Process Industries  
**Project Title**: Customer Conversion Analysis for Online Shopping Using Clickstream Data

---

## 👨‍🎓 Project Team

- **S. Santhiya** – 110523237023  
- **S. Selvarani** – 110523237025  
- **S. Shivani Keerthana** – 110523237026  
- **S. Vaithiswari** – 110523237029  
- **B. Varshini** – 110523237030

---

## 🚀 Project Overview

This project replicates a real-world business scenario faced by e-commerce platforms (e.g., Amazon, Flipkart). We analyze user clickstream behavior to:

- 🧠 Predict whether a customer will complete a purchase  
- 💰 Estimate potential revenue per session  
- 👥 Segment customers based on browsing patterns  

The solution is deployed using a user-friendly **Streamlit** interface.

---

## 📊 Business Objectives

- 🎯 Predict customer conversions  
- 📈 Forecast revenue generation from users  
- 👥 Segment users for personalized targeting  
- 🛒 Minimize customer drop-off and bounce rates  
- 🤖 Enable data-driven recommendations  

---

## 🧰 Tools & Technologies

- **Programming Language**: Python  
- **Libraries**: Pandas, NumPy, Scikit-learn, XGBoost, Seaborn, Matplotlib  
- **ML Models**: Logistic Regression, Decision Trees, Random Forest, XGBoost, KMeans, Linear Regression  
- **Visualization**: Streamlit Web App  
- **Data Source**: UCI Clickstream Data  

---

## 🗃️ Dataset Overview

The dataset contains user session data such as:

- Country, Page Number, Product Price  
- Model Photography, Product Category, Product Color  
- Session Time, Revisit Behavior, Page Position  

---

## 🧠 Machine Learning Approaches

### Classification
- Logistic Regression  
- Decision Tree  
- Random Forest  
- XGBoost  
- Neural Networks

### Regression
- Linear Regression  
- Ridge, Lasso  
- Gradient Boosting Regressor

### Clustering
- KMeans  
- DBSCAN  
- Hierarchical Clustering

---

## 📈 Evaluation Metrics

| Model Type     | Metrics Used                          |
|----------------|----------------------------------------|
| Classification | Accuracy, F1-Score, Precision, ROC-AUC |
| Regression     | MAE, MSE, RMSE, R²                     |
| Clustering     | Silhouette Score, DBI, CH Score        |

---

## 🖥️ Streamlit Web Application

Features:
- Upload your dataset (.csv)  
- Predict conversion probability  
- Estimate session-wise revenue  
- Visualize clusters with charts  
- Real-time classification and regression output  

Run locally:
```bash
streamlit run app.py
