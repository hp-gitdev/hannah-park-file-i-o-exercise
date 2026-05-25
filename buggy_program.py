# buggy_program.py — Contains 4 bugs. Find and fix them all.

def calculate_stats(numbers):          #missing colons - SyntaxError
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    
    above_average = []
    for num in numbers:
        if num > average:           #missing colons - SyntaxError
            above_average.append(num)
    
    return {
        "total": total,
        "average": average,
        "above_average": above_average,
        "above_count": len(above_average)
    }

scores = [85, 92, 78, 95, 88, 70, 93] #included string - TypeError
result = calculate_stats(scores)

print(f"Total: {result['total']}")
print(f"Average: {result['average']}") #missing single quote - NameError
print(f"Above average: {result['above_count']} scores")

#found ALL of the bugs by myself!



#AI made my inventory.py more Pythonic:

inventory = {
    "laptop": {"price": 999.99, "quantity": 15},
    "mouse": {"price": 29.99, "quantity": 50},
    "headphone": {"price": 129.99, "quantity": 60},
    "deskpad": {"price": 39.99, "quantity": 40},
}

LOW_STOCK_THRESHOLD = 10


def find_product(prompt):
    """Ask for a product name and return (cleaned_name, info_dict_or_None)."""
    name = input(prompt).strip().lower()
    return name, inventory.get(name)


# --- Inventory table with totals ---
print(f"{'Product':<15} {'Price':<10} {'Quantity':<10} {'Total':<10}")
print("-" * 45)

for product, info in inventory.items():
    line_total = info["price"] * info["quantity"]
    print(f"{product:<15} ${info['price']:9.2f} {info['quantity']:10} {line_total:9.2f}")

total = sum(info["price"] * info["quantity"] for info in inventory.values())
print("-" * 45)
print(f"{'Total Value of Inventory':<37} ${total:.2f}")


# --- Look up a product ---
search, product = find_product("\nLook up the item: ")
if product:
    print(f"\nFound: {search}")
    print(f"Price: {product['price']}")
    print(f"Quantity: {product['quantity']}")
else:
    print(f"No product found for '{search}'.")


# --- Update a quantity (with validation) ---
search, product = find_product("\nWhich product needs an update? ")
if product:
    print(f"Current quantity of {search} is {product['quantity']}.")
    raw = input(f"Enter the new quantity for {search}: ").strip()
    if raw.isdigit():
        product["quantity"] = int(raw)
        print(f"Updated: The quantity of {search} is now {product['quantity']}.")
    else:
        print("Please enter a whole number. No changes made.")
else:
    print(f"No product found for '{search}'.")


# --- Check stock status ---
low_stock = {p for p, info in inventory.items() if info["quantity"] < LOW_STOCK_THRESHOLD}

check, product = find_product("\nCheck stock status for which product? ")
if check in low_stock:
    print(f"Need to reorder {check}!")
elif product:
    print(f"{check} is well stocked.")
else:
    print(f"No product found for '{check}'.")