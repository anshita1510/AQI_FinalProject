import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Air Quality Index (AQI) Dashboard")

uploaded_file = st.file_uploader("air_quality.csv", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.dataframe(df)

    st.subheader("Data Preview (5 rows)")
    st.dataframe(df.head())
    st.subheader("Basic Statistics")
    st.write(df.describe())

    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))

    numeric_df = df.select_dtypes(include=['number'])
    sns.heatmap(numeric_df.corr(), annot=True, cmap="viridis", ax=ax)
    st.pyplot(fig)

