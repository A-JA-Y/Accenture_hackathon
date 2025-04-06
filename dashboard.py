import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Retail Inventory Optimization Dashboard", layout="wide")


inventory_data = pd.read_csv("data/inventory_monitoring.csv")
demand_data = pd.read_csv("data/demand_forecasting.csv")
pricing_data = pd.read_csv("data/pricing_optimization.csv")

st.title("📦 Multi-Agent Inventory Optimization")


st.subheader("Store Inventory Overview")
store_id = st.selectbox("Select Store", inventory_data['Store ID'].unique())
filtered_data = inventory_data[inventory_data['Store ID'] == store_id]

st.dataframe(filtered_data[['Product ID', 'Stock Levels', 'Reorder Point', 'Supplier Lead Time (days)']])


product_id = st.selectbox("Select Product for Demand Trend", demand_data['Product ID'].unique())
product_demand = demand_data[
    (demand_data['Product ID'] == product_id) &
    (demand_data['Store ID'] == store_id)
]

st.subheader("📈 Historical Demand Trend")
fig, ax = plt.subplots()
ax.plot(product_demand['Date'], product_demand['Sales Quantity'], marker='o')
ax.set_xlabel("Date")
ax.set_ylabel("Sales Quantity")
ax.set_title(f"Sales Trend for Product {product_id} at Store {store_id}")
st.pyplot(fig)
