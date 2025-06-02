import streamlit as st
import pandas as pd
from io import StringIO


st.markdown("""
    <style>
        .main-title {
            font-size: 28px;
            font-weight: bold;
            color: #1d3557;
            text-align: center;
            margin-bottom: 25px;
        }
        .section-title {
            font-size: 20px;
            color: #2c3e50;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Upload and Analyze Emails</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    language = st.selectbox("Select Language", ["English", "العربية", "Türkçe"])

with col2:
    model_choice = st.selectbox("Choose Model", ["Naive Bayes", "Random Forest", "Logistic Regression"])

st.markdown('<div class="section-title">Upload Email Dataset (CSV)</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    df = pd.read_csv(stringio)

    st.markdown('<div class="section-title">Uploaded Data</div>', unsafe_allow_html=True)
    st.dataframe(df)

    if st.button("Run Analysis"):
        df['Prediction'] = ["Phishing" if i % 2 == 0 else "Legit" for i in range(len(df))]

        st.markdown('<div class="section-title">Analysis Results</div>', unsafe_allow_html=True)
        st.dataframe(df)

        st.download_button("Download PDF Report", data="PDF content here...", file_name="email_analysis_report.pdf")