# app.py
import streamlit as st
from gspread_dataframe import set_with_dataframe
import gspread as gd
import pandas as pd

def main():
    # Create Streamlit app
    st.title("Data Marketplace Update")

    # SHOPEE
    st.header("SHOPEE Data Upload")
    shopee_file = st.file_uploader("Upload SHOPEE Excel file", type=["xlsx"])
    if shopee_file:
        shopee_data = pd.read_excel(shopee_file, sheet_name='orders')
        st.write(shopee_data)  # Display the data (optional)
        st.success("SHOPEE data uploaded successfully!")

    # TOKOPEDIA
    st.header("TOKOPEDIA Data Upload")
    tokopedia_file = st.file_uploader("Upload TOKOPEDIA Excel file", type=["xlsx"])
    if tokopedia_file:
        tokopedia_data = pd.read_excel(tokopedia_file, sheet_name='Laporan Penjualan', skiprows=4, usecols="A:AP")
        st.write(tokopedia_data)  # Display the data (optional)
        st.success("TOKOPEDIA data uploaded successfully!")

    # LAZADA
    st.header("LAZADA Data Upload")
    lazada_file = st.file_uploader("Upload LAZADA Excel file", type=["xlsx"])
    if lazada_file:
        lazada_data = pd.read_excel(lazada_file, sheet_name='sheet1')
        st.write(lazada_data)  # Display the data (optional)
        st.success("LAZADA data uploaded successfully!")

if __name__ == "__main__":
    main()
