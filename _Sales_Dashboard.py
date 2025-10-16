import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def show_dashboard():
    st.title("📊 BigMart Sales Dashboard")

    # Load dataset
    df = pd.read_excel("cleaned_bigmart.xlsx")

    # Sidebar Filters
    st.sidebar.header("🔍 Filter Options")

    if 'Outlet_Type' in df.columns:
        outlet_type = st.sidebar.multiselect(
            "Select Outlet Type",
            options=df['Outlet_Type'].unique(),
            default=df['Outlet_Type'].unique()
        )
        df = df[df['Outlet_Type'].isin(outlet_type)]

    if 'Item_Type' in df.columns:
        item_type = st.sidebar.multiselect(
            "Select Item Type",
            options=df['Item_Type'].unique(),
            default=df['Item_Type'].unique()
        )
        df = df[df['Item_Type'].isin(item_type)]

    # Layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Sales Distribution")
        fig = px.histogram(df, x="Item_Outlet_Sales", nbins=30, color_discrete_sequence=["skyblue"])
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Average Sales by Item Type")
        avg_sales = df.groupby("Item_Type")["Item_Outlet_Sales"].mean().sort_values(ascending=False)
        fig = px.bar(
            x=avg_sales.index, y=avg_sales.values,
            labels={'x': 'Item Type', 'y': 'Average Sales'},
            color=avg_sales.values, color_continuous_scale="Greens"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Sales by Outlet Type")
    fig = px.box(df, x="Outlet_Type", y="Item_Outlet_Sales", color="Outlet_Type")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Correlation Heatmap")
    corr = df.corr(numeric_only=True)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, cmap="YlGnBu", annot=True, fmt=".2f", ax=ax)
    st.pyplot(fig)
