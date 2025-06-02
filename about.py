import streamlit as st


st.markdown("""
    <style>
        .main-title {
            font-size: 28px;
            font-weight: bold;
            color: #1d3557;
            text-align: center;
            margin-bottom: 25px;
        }
        .paragraph {
            font-size: 16px;
            color: #2c3e50;
            text-align: justify;
            line-height: 1.6;
            margin-bottom: 20px;
        }
        .credit {
            font-size: 14px;
            color: #4d4d4d;
            text-align: center;
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">About the Project</div>', unsafe_allow_html=True)

st.markdown('<div class="paragraph">This project, titled <b>"Detection and Countermeasures Using Machine Learning"</b>, focuses on the detection of phishing emails using various machine learning models. The project was developed as part of a master's thesis in Cybersecurity at Bahçeşehir University, Turkey.</div>', unsafe_allow_html=True)

st.markdown('<div class="paragraph">The system allows for uploading email datasets, analyzing them with multiple classification models including Naive Bayes, Random Forest, and Logistic Regression, and generating detailed reports. The interface supports three languages: Arabic, English, and Turkish.</div>', unsafe_allow_html=True)

st.markdown('<div class="paragraph">Phishing is one of the most prevalent cybersecurity threats today. By applying machine learning techniques, this project aims to enhance detection accuracy and raise awareness of adversarial risks in email communication.</div>', unsafe_allow_html=True)

st.markdown('<div class="credit">Developed by: Nainwa Ahmad Hayajneh – MSc in Cybersecurity</div>', unsafe_allow_html=True)