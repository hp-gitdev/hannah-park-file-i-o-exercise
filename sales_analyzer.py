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
        revenue_per_product[product] = 0
    revenue_per_product[product] += row_revenue   

   
    if quantity not in quantity_per_product:
        quantity_per_product[product] = 0
    quantity_per_product[product] += quantity

    if date not in revenue_per_day:
        revenue_per_day[date] = 0
    revenue_per_day[date] += row_revenue


highest_total_revenue = max(revenue_per_day, key=revenue_per_day.get)

with open("sales_report.txt", "w") as file:
    file.write("SALES REPORT\n")
    file.write("=" * 40 + "\n")
    file.write(f"Total Revenue: {total_revenue:.2f}\n\n") 
    file.write("Revenue Per Product:\n")
    for product, revenue in revenue_per_product.items():
        file.write(f"{product}: ${revenue:.2f}\n")
    file.write("\n")

    file.write(f"Total Quantity Sold Per Product:\n")
    for product, quantity in quantity_per_product.items():
        file.write(f" {product}: {quantity}\n") 
    file.write("\n")

    file.write(f"Highest Total Revenue: {highest_total_revenue} ${revenue_per_day[highest_total_revenue]:.2f}\n")

with open("product_summary.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["product", "total_quantity", "total_revenue"])
    writer.writeheader()

    for product, quantity in quantity_per_product.items():
        revenue = revenue_per_product[product] 
        writer.writerow({
        "product": product,
        "total_quantity": quantity,
        "total_revenue": round(revenue, 2)
        })

def main():
    students = load_students("data/students.csv")

    print(f"Loaded {len(students)} students.")

    report = generate_report(students)

    print_summary(report)

    write_report(report, "grade_report.txt")

    print("Class Report")

if __name__ = "__main__":
    main()       