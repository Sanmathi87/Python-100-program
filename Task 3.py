import pandas as pd

# Create data directly in Python (no CSV file)
data = {
    "OrderID": [101, 102, 103, 104, 105, 106],
    "Customer": ["Asha", "Rohan", "Meena", "Karthik", "Divya", "Arun"],
    "Category": ["Electronics", "Clothing", "Electronics", "Grocery", "Clothing", "Electronics"],
    "Amount": [45000, 2500, 38000, 1200, 5200, 28000],
    "Status": ["Delivered", "Cancelled", "Delivered", "Delivered", "Delivered", "Delivered"],
    "City": ["Chennai", "Madurai", "Coimbatore", "Salem", "Trichy", "Chennai"]
}

# Convert dictionary to DataFrame
orders = pd.DataFrame(data)

print("ALL ORDERS:")
print(orders)

# Filter: Delivered orders only
print("\nDELIVERED ORDERS:")
delivered_orders = orders[orders["Status"] == "Delivered"]
print(delivered_orders)

# Filter: High-value orders (Amount > 10000)
print("\nHIGH VALUE ORDERS (Amount > 10000):")
high_value_orders = orders[orders["Amount"] > 10000]
print(high_value_orders)

# Multiple condition filtering
print("\nPREMIUM ELECTRONICS ORDERS:")
premium_electronics = orders[
    (orders["Category"] == "Electronics") &
    (orders["Amount"] > 30000) &
    (orders["Status"] == "Delivered")
]
print(premium_electronics)

# Column-based filtering
print("\nDELIVERED ORDERS (Customer & Amount only):")
result = orders.loc[orders["Status"] == "Delivered", ["Customer", "Amount"]]
print(result)
