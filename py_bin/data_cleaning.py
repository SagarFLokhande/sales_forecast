# Python program to generate time series data for the sales of a supermarket. This file cleans the raw data.

# First import all modules we expect to use
import numpy as np, pandas as pd

def cleaned_furn_data(fname: str):
    """ This function will take a hige Excel sheet as data and return cleaned data for a specific category, here "Furniture"."""
    df = pd.read_excel(fname)
    furniture = df.loc[ df["Category"] == "Furniture" ] 
    print( "Earliest date for Furniture data: ", furniture["Order Date"].min() )
    print( "Latest date for Furniture data: ", furniture["Order Date"].max() )
    cols = ["Row ID", "Order ID", "Ship Date", "Ship Mode", "Customer ID", "Customer Name", "Segment", "Country", "City", "State", "Postal Code", "Region", "Product ID", "Category", "Sub-Category", "Product Name", "Quantity", "Discount", "Profit"]
    newfurn = furniture.drop(cols, axis="columns")
    newfurn = newfurn.sort_values("Order Date")
    newfurn.isnull().sum()
    newfurn = newfurn.groupby("Order Date")["Sales"].sum().reset_index()
    return newfurn





