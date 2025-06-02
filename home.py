import streamlit as st

st.markdown("""
    <style>
        .main-title {
            font-size: 32px;
            font-weight: bold;
            color: #1d3557;
            text-align: center;
            margin-bottom: 30px;
        }
        .paragraph {
            font-size: 18px;
            color: #2c3e50;
            text-align: justify;
            margin: 0 10%;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Welcome to the Phishing Detection App</div>', unsafe_allow_html=True)

st.markdown('<div class="paragraph">This application helps classify email messages as either legitimate or phishing using machine learning models. You can analyze emails, view model statistics, and download detailed PDF reports. The interface supports English, Arabic, and Turkish for broader accessibility.</div>', unsafe_allow_html=True)