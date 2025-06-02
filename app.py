
import streamlit as st

st.set_page_config(page_title="Phishing Detection App", layout="wide")

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "Upload & Analyze", "Statistics", "About"])

if selection == "Home":
    import home
elif selection == "Upload & Analyze":
    import upload_analyze
elif selection == "Statistics":
    import statistics
elif selection == "About":
    import about
