import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Product Price Trend")

df = pd.read_csv('products.csv')

df['ModifyDate'] = pd.to_datetime(df['ModifyDate'], errors='coerce')
df = df.dropna(subset=['ModifyDate'])

monthly = (
    df.groupby(df['ModifyDate'].dt.to_period('M'))['Price']
      .mean()
      .reset_index()
)

monthly['ModifyDate'] = monthly['ModifyDate'].dt.to_timestamp()

fig = px.line(
    monthly,
    x='ModifyDate',
    y='Price',
    markers=True
)

st.plotly_chart(fig, use_container_width=True)
