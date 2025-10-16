import streamlit as st
import _Sales_Dashboard
import _Sales_Prediction

# Page configuration
st.set_page_config(
    page_title="BigMart Sales App",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Sidebar Navigation ---
st.sidebar.title("📂 Navigation")
page = st.sidebar.radio(
    "Go to:",
    ["Home", "Sales Dashboard", "Sales Prediction"],
    key="selected_page"
)

# --- HOME PAGE ---
if page == "Home":
    st.title("🏪 BigMart Sales Analysis & Prediction App")
    st.markdown("""
    Welcome!  
    This app has two sections:
    - 📊 *Sales Dashboard* – Interactive visual analysis of sales data  
    - 🤖 *Sales Prediction* – Predict outlet sales using a trained Random Forest model  

    """)

# --- SALES DASHBOARD PAGE ---
elif page == "Sales Dashboard":
    _Sales_Dashboard.show_dashboard()

# --- SALES PREDICTION PAGE ---
elif page == "Sales Prediction":
    _Sales_Prediction.show_prediction()

