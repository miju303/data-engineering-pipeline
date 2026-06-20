import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# --- Page setup ---
st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📊 Sales Performance Dashboard")

# --- Connect to PostgreSQL and load data ---
@st.cache_data
def load_data():
    engine = create_engine("postgresql://postgres:miju@localhost:5432/salesdb")
    df = pd.read_sql("SELECT * FROM orders", engine)
    df["order_date"] = pd.to_datetime(df["order_date"])
    return df

df = load_data()

# --- Sidebar filters ---
st.sidebar.header("Filters")
years = sorted(df["year"].unique())
selected_year = st.sidebar.selectbox("Select Year", options=["All"] + list(years))

regions = sorted(df["region"].unique())
selected_region = st.sidebar.multiselect("Select Region(s)", options=regions, default=regions)

filtered_df = df.copy()
if selected_year != "All":
    filtered_df = filtered_df[filtered_df["year"] == selected_year]
filtered_df = filtered_df[filtered_df["region"].isin(selected_region)]

# --- Key Metrics ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${filtered_df['sales'].sum():,.0f}")
col2.metric("Total Profit", f"${filtered_df['profit'].sum():,.0f}")
col3.metric("Total Orders", f"{filtered_df['order_id'].nunique():,}")
col4.metric("Avg Order Value", f"${filtered_df['sales'].mean():,.2f}")

st.markdown("---")

# --- Charts ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales by Category")
    sales_by_category = filtered_df.groupby("category")["sales"].sum().sort_values(ascending=False)
    st.bar_chart(sales_by_category)

with col2:
    st.subheader("Sales by Region")
    sales_by_region = filtered_df.groupby("region")["sales"].sum().sort_values(ascending=False)
    st.bar_chart(sales_by_region)

st.subheader("Sales Trend Over Time")
sales_by_year = filtered_df.groupby(filtered_df["order_date"].dt.year)["sales"].sum()
st.line_chart(sales_by_year)

st.subheader("Top 10 Products by Sales")
top_products = filtered_df.groupby("product_name")["sales"].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_products)

st.markdown("---")
st.subheader("Raw Data Preview")
st.dataframe(filtered_df.head(100))