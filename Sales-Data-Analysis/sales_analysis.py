# --------------------------
# sales Data Analysis Project
# Author: Sakshi Kashyap
# --------------------------

#import pandas
import pandas as pd

# --------------------------
# STEP 1: lOAD DATASET
# --------------------------
df = pd.read_csv('sales_data.csv')
# print(df.head()) 
print("=" * 50)
print("SALES DATA ANALYSIS")
print("=" * 50)
# --------------------------
# STEP 2: EXPLORE DATA
# --------------------------

print("\nDataset Shape")
print(df.shape)

print("\ncolumns")
print(df.columns)

print("\nData Types")
print(df.dtypes)

print("\nFirst 5 ROws")
print(df.head())

# --------------------------
# STEP 3: check missing value
# --------------------------

print("\nmissing value")
print(df.isnull().sum())

# fill missing numeric values
numeric_cols = df.select_dtypes(include="number").columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())
    
# fill misiing text values with unknown
text_cols = df.select_dtypes(include="object").columns

for col in text_cols:
    df[col] = df[col].fillna("Unknown")
    
# --------------------------------------------
# STEP 4: Remove Duplicate Rows
# --------------------------------------------

duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows: {duplicates}")

df = df.drop_duplicates()

# --------------------------------------------
# STEP 5: Calculate Metrics
# --------------------------------------------

# Total Revenue
total_revenue = df["Total_Sales"].sum()

# Total Quantity Sold
total_quantity = df["Quantity"].sum()

# Average Sale
average_sale = df["Total_Sales"].mean()

# Highest Sale
highest_sale = df["Total_Sales"].max()

# Lowest Sale
lowest_sale = df["Total_Sales"].min()

# --------------------------------------------
# STEP 6: Best Selling Product
# --------------------------------------------

best_product = (
    df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

# Revenue by Product
revenue_by_product = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

# Revenue by Region
region_sales = (
    df.groupby("Region")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

# --------------------------------------------
# STEP 7: Print Report
# --------------------------------------------

print("\n" + "=" * 50)
print("SALES REPORT")
print("=" * 50)

print(f"Total Revenue      : ₹{total_revenue:,.2f}")
print(f"Total Quantity     : {total_quantity}")
print(f"Average Sale       : ₹{average_sale:,.2f}")
print(f"Highest Sale       : ₹{highest_sale:,.2f}")
print(f"Lowest Sale        : ₹{lowest_sale:,.2f}")

print("\nBest Selling Product")
print(best_product)

print("\nRevenue by Product")
print(revenue_by_product)

print("\nRevenue by Region")
print(region_sales)

print("\nAnalysis Completed Successfully!")