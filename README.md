**Product Price Trend Analysis

This project demonstrates an end-to-end data analysis workflow using NumPy, Pandas, data cleaning techniques, data visualization, and a basic Streamlit application. The main objective is to analyze product-related datasets and visualize price trends over time in an interactive format.

**Project Overview

The project covers:

NumPy operations for numerical analysis

Pandas for data loading, cleaning, and transformation

Data visualization using Plotly

A basic Streamlit web app to display a monthly product price trend line chart

** Datasets Used

The following datasets are used in this project:

products.csv / products.xls – Product details including prices and modified dates

categories.csv – Product category information

customers.csv – Customer data

employees.csv – Employee details

cities.csv – City-level data

countries.csv – Country information

These datasets are used to perform data cleaning, aggregation, and analysis operations.

** Data Cleaning & Processing

Handled missing and invalid values

Converted date columns to proper datetime format

Removed null records

Grouped data by month and calculated average prices

 **Data Visualization

Interactive line chart using Plotly

Monthly average product price trend

Clean and responsive visualization

** Streamlit Application

A simple Streamlit app is built to visualize product price trends.

** Technologies Used

Python

NumPy

Pandas

Plotly

Streamlit

**Streamlit Code
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

**How to Run the Project

Clone the repository

Install required libraries:

pip install numpy pandas plotly streamlit


Keep app.py and products.csv in the same folder

Run the Streamlit app:

streamlit run app.py

**Key Learnings

Practical experience with real-world datasets

Hands-on use of NumPy and Pandas

Creating interactive visualizations with Plotly

Building and running a basic Streamlit application
