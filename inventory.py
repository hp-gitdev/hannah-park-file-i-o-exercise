
inventory = {   
    "laptop": {"price": 999.99, "quantity": 15},
    "mouse": {"price": 29.99, "quantity": 50},
    "headphone": {"price": 129.99, "quantity": 60},
    "deskpad": {"price": 39.99, "quantity": 40}
}


print("=" * 35)
print("Inventory Table".center(35))
print("=" * 35)

print(f"{'Product':15}{'Price':10}{'Quantity':10}")

print("-" * 35)

for product, info in inventory.items():
    print(f"{product:15} ${info['price']:<9.2f} {info['quantity']:<10}")

print("-" * 35)


print("\n")

print(f"{'Product':<15} {'Price':<10} {'Quantity':<10} {'Total':<10}")
print("-" * 45)

total = 0
for product, info in inventory.items():
    line_total = info['price'] * info['quantity'] 
    total += line_total
    print(f"{product:<15} ${info['price']:9.2f} {info['quantity']:10} {line_total:9.2f}")


print("-" * 45)
print(f"{'Total Value of Inventory':<37} ${total:.2f}")

search = input("\nLook up the item: ").lower()
product = inventory.get(search) 

if product:
    print(f"\nFound: {search}")
    print(f"Price: {product['price']}")
    print(f"Quantity: {product['quantity']}")
else:
    print(f"No product found for '{search}'.")


search = input("\nWhich product needs an update?").lower()
product = inventory.get(search)

if product:
    change = int(input(f"what is a current quantity for {search}: "))
    product['quantity'] = change
    print(f"Updated: The quantity of {search} is now {product['quantity']}.")
else:
    print(f"No product found for '{search}.'")    


low_stock = {product for product, info in inventory.items() if info['quantity']<10}

check = input("\nCheck stock status for which product? ").lower()

if check in low_stock:
    print(f"Need to reorder {check}!")
elif check in inventory:
    print(f"{check} is well stocked.")
else:
    print(f"No product found for '{check}.'")
