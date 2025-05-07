import streamlit as st
import pandas as pd
from app.preprocessing import preprocess_data
from app.modeling import train_classification_model, train_regression_model, train_clustering_model

st.title("🛒 Clickstream Customer Conversion Analysis")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
task = st.selectbox("Select Task", ["Classification", "Regression", "Clustering"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("📊 Raw Data", df.head())

    processed_df = preprocess_data(df)

    if task == "Classification":
        target = st.selectbox("Select Target Variable", df.columns)
        X = processed_df.drop(target, axis=1)
        y = df[target]

        model = train_classification_model(X, y)
        preds = model.predict(X)
        st.write("✅ Classification Done. Predictions:", preds[:5])

    elif task == "Regression":
        target = st.selectbox("Select Target Variable", df.columns)
        X = processed_df.drop(target, axis=1)
        y = df[target]

        model = train_regression_model(X, y)
        preds = model.predict(X)
        st.write("💰 Revenue Predictions:", preds[:5])

    elif task == "Clustering":
        model, clusters = train_clustering_model(processed_df)
        df['Cluster'] = clusters
        st.write("👥 Customer Segments", df[['Cluster']].value_counts())
        st.dataframe(df)
