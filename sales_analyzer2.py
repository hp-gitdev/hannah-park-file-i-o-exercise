import csv

sales = []
with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["quantity"] = int(row["quantity"])
        row["price"] = float(row["price"])
        sales.append(row)

total_revenue = 0
revenue_per_product = {}
quantity_per_product = {}
revenue_per_day = {}

for sale in sales:
    product = sale["product"]
    quantity = sale["quantity"]
    price = sale["price"]
    date = sale["date"]
    row_revenue = quantity * price

    total_revenue += row_revenue

    if product not in revenue_per_product:
        revenue_per_product[product]= 0
    revenue_per_product[product] += row_revenue

    if quantity not in revenue_per_product:
        revenue_per_product[quantity] = 0
    revenue_per_product[quantity] += quantity

    if date not in revenue_per_day:
        revenue_per_product[date] = 0
    revenue_per_day += row_revenue

highest_total_revenue = max(revenue_per_day, key = revenue_per_day.get)