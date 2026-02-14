import pandas as pd


# Creating DataFrames
df_products = pd.DataFrame({
    "ProductID": [1, 2, 3, 4, 5],
    "ProductName": ["Rice", "Milk", "Bread", "Oil", "Sugar"],
    "Category": ["Grocery", "Dairy", "Bakery", "Grocery", "Grocery"],
    "CostPrice": [40, 20, 25, 120, 35]
})

df_sales = pd.DataFrame({
    "ProductID": [1, 2, 3, 4, 5],
    "QuantitySold": [50, 120, 80, 40, 60],
    "SellingPrice": [55, 30, 40, 150, 50]
})


# Merging
df = pd.merge(df_products, df_sales, on="ProductID")
print("\nMERGED DATAFRAME")
print(df)


# Filtering
print("\nFILTERED DATA (Grocery Category)")
print(df[df["Category"] == "Grocery"])

print("\nPRODUCTS WITH QUANTITY SOLD > 50")
print(df[df["QuantitySold"] > 50])



# Sorting
print("\nSORTED BY QUANTITY SOLD (DESCENDING)")
print(df.sort_values(by="QuantitySold", ascending=False))


# Grouping
print("\nCATEGORY WISE TOTAL QUANTITY SOLD")
print(df.groupby("Category")["QuantitySold"].sum())

