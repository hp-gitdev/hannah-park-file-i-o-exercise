inventory = {
    "laptop": {"price": 999.99, "quantity": 15},
    "mouse": {"price": 29.99, "quantity": 50},
    "headphones": {"price": 129.99, "quantity": 30},
    "deskpad": {"price": 49.99, "quantity": 40},
}

print("=" *45)
print("Inventory".center(45))
print("=" *45)

print(f"{'Product':15} {'Price':10} {'Qauntity':10}")

for product, info in inventory.items():
    print(f"{product:10}: {info['price']:<15.2f} {info['quantity']:<15}")

print("-" *45)

print(f"{'Product':15} {'Price':10} {'Qauntity':10} {'Total'}")

total = 0

for product, info in inventory.items():
    line_total = info['price'] * info['quantity']
    total += line_total 
    print(f"{product:10}: ${info['price']:<15.2f} {info['quantity']:<15} {line_total:.2f}")

print("-" *45)
 
print(f"Total value of the inventory: {total:.2f}")


search = input("What product are you looking for? ").lower()

product = inventory.get(search)
    
if product:
    print(f"Found:{search}, price:${product['price']}, qty: {product['quantity']}")
    
else:
    print(f"Invalid product of {search}.")


search = input("\nWhat product do you want to update? ").lower()

product = inventory.get(search)

if inventory:
   change = int(input(f"\nWhat is a current quantity of {search}?" ))
   product['quantity'] = change

   print(f"\nUpdated product: {search}   Quantity: {product['quantity']}")

else:
    print(f"\nNo {search} found in the inventory.")



low_stock = set()

for product, info in inventory.items():
    if info['quantity']<10:
        low_stock.add(product)
        print(f"{product} requires a re-stock!!")
    
if not low_stock:
        print("No re-stock necessary at this point.")