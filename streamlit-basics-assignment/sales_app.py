import streamlit as st
import pandas as pd
# TASK - 1
# -------------------------------
# Title and description
# -------------------------------
st.title("📊 Sales Summary Dashboard")
st.subheader("Quick overview of product sales with category filtering")

# -------------------------------
# Hardcoded dataset
# -------------------------------
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Monitor","Charger"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Electronics", "Accessories"],
    "Sales": [1500, 800, 600, 200, 1200, 300]
}

df = pd.DataFrame(data)

# -------------------------------
# Selectbox filter
# -------------------------------

# Get unique categories
categories = df["Category"].unique()

# Create selectbox
selected_category = st.selectbox("Select Category", categories)

# Filter dataframe
filtered_df = df[df["Category"] == selected_category]

# Display filtered data
st.dataframe(filtered_df)

# TASK - 2
# -------------------------------
# Sidebar filter
# -------------------------------
st.sidebar.header("Filter Options")

selected_category1 = st.sidebar.selectbox("Select Category", categories)

# -------------------------------
# Filter data
# -------------------------------
filtered_df = df[df["Category"] == selected_category1]

# -------------------------------
# Display results
# -------------------------------
st.write(f"### Showing data for category: {selected_category1}")

st.dataframe(filtered_df)

# -------------------------------
# Line chart
# -------------------------------
st.write("### Sales Trend")
st.line_chart(filtered_df["Sales"])