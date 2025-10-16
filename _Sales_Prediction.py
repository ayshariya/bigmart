import streamlit as st
import pandas as pd
import pickle
import numpy as np

#Load model, scaler, and dataset only once
@st.cache_resource
def load_resources():
    model = pickle.load(open("big_mart.pkl", "rb"))
    x_columns = pickle.load(open("x_columns.pkl", "rb"))
    scaler = pickle.load(open("scaler.pkl", "rb"))
    df = pd.read_excel("cleaned_bigmart.xlsx")
    return model, scaler, df

def show_prediction():
    st.title("🤖 BigMart Sales Prediction (Random Forest Model)")

# Load resources
    model, scaler, df = load_resources()

# Drop target column
    if "Item_Outlet_Sales" in df.columns:
        X = df.drop("Item_Outlet_Sales", axis=1)
    else:
        X = df.copy()

# Collect user input
    st.subheader("Enter Details to Predict Sales")

    col1, col2, col3 = st.columns(3)
    with col1:
        item_weight = st.number_input("Item Weight", min_value=0.0)
        item_visibility = st.number_input("Item Visibility", min_value=0.0)
    with col2:
        item_mrp = st.number_input("Item MRP", min_value=0.0)
        outlet_size = st.selectbox("Outlet Size", df["Outlet_Size"].unique())
    with col3:
        outlet_type = st.selectbox("Outlet Type", df["Outlet_Type"].unique())
        outlet_location = st.selectbox("Outlet Location Type", df["Outlet_Location_Type"].unique())

# Create DataFrame for user input
    user_data = pd.DataFrame({
        "Item_Weight": [item_weight],
        "Item_Visibility": [item_visibility],
        "Item_MRP": [item_mrp],
        "Outlet_Size": [outlet_size],
        "Outlet_Type": [outlet_type],
        "Outlet_Location_Type": [outlet_location]
    })
    st.write("### Your Input:")
    st.dataframe(user_data)

# Predict sales
    #if st.button("🔮 Predict Sales"):
        #user_data_encoded = pd.get_dummies(user_data)

# Ensure user_data has same columns as training data
       # missing_cols = set(x_columns) - set(user_data_encoded.columns)
    #for col in missing_cols:
        #user_data_encoded[col] = 0
       # user_data_encoded = user_data_encoded[x_columns] 
   

    # Scale and predict
   # user_data_scaled = scaler.transform(user_data_encoded)
   # prediction = model.predict(user_data_scaled)
    #st.success(f"💰 Predicted Sales: ₹{prediction[0]:.2f}")