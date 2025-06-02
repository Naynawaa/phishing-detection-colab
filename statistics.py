import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


st.markdown("""
    <style>
        .main-title {
            font-size: 28px;
            font-weight: bold;
            color: #1d3557;
            text-align: center;
            margin-bottom: 20px;
        }
        .sub-section {
            font-size: 20px;
            color: #2c3e50;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Model Performance Statistics</div>', unsafe_allow_html=True)

data = {
    "Model": ["Naive Bayes", "Random Forest", "Logistic Regression"],
    "Accuracy": [0.93, 0.96, 0.94],
    "Precision": [0.91, 0.95, 0.92],
    "Recall": [0.89, 0.97, 0.91],
    "F1 Score": [0.90, 0.96, 0.91]
}
df = pd.DataFrame(data)

st.markdown('<div class="sub-section">Evaluation Metrics</div>', unsafe_allow_html=True)
st.dataframe(df.style.format("{:.2%}"))

st.markdown('<div class="sub-section">Model Comparison Chart</div>', unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(10, 5))
bar_width = 0.2
index = range(len(df))

ax.bar([i - bar_width for i in index], df['Accuracy'], width=bar_width, label='Accuracy')
ax.bar(index, df['Precision'], width=bar_width, label='Precision')
ax.bar([i + bar_width for i in index], df['Recall'], width=bar_width, label='Recall')
ax.bar([i + 2*bar_width for i in index], df['F1 Score'], width=bar_width, label='F1 Score')

ax.set_xticks(index)
ax.set_xticklabels(df['Model'])
ax.set_ylabel("Score")
ax.set_title("Model Metrics Comparison")
ax.legend()

st.pyplot(fig)