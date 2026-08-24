import csv
import random

# Set a "seed" so the random data is the same every time we run this
random.seed(42)

# Fictional product catalog for Bharani's Retail & Co.
categories = ["Electronics", "Home & Kitchen", "Toys", "Sportswear", "Stationery"]
product_names = [
    "Wireless Earbuds", "Desk Lamp", "Building Blocks Set", "Yoga Mat", "Notebook Pack",
    "Bluetooth Speaker", "Coffee Maker", "Remote Control Car", "Running Shoes", "Sticky Notes",
    "Smart Watch", "Air Fryer", "Puzzle Set", "Water Bottle", "Highlighter Pack",
    "Laptop Stand", "Blender", "Action Figure", "Resistance Bands", "Sketch Pad"
]
suppliers = ["Nova Supplies", "Orbit Traders", "Peak Distributors", "Summit Wholesale"]

# Generate 50 fictional products
rows = []
for i in range(1, 51):
    product = {
        "product_id": f"P{i:03d}",                          # e.g. P001, P002...
        "product_name": random.choice(product_names),
        "category": random.choice(categories),
        "supplier": random.choice(suppliers),
        "unit_cost": round(random.uniform(5, 150), 2),
        "unit_price": round(random.uniform(10, 300), 2),
        "stock_quantity": random.randint(0, 500),
        "units_sold_last_month": random.randint(0, 200),
    }
    rows.append(product)

# Write the data to a CSV file
with open("inventory_data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("✅ inventory_data.csv created with", len(rows), "products.")