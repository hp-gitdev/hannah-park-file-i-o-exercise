

item1_name = "Notebook"
item1_price = "4.99"
item1_qty = "2"

item2_name = "Pen Pack"
item2_price = "7.50"
item2_qty = "1"

item3_name = "Backpack"
item3_price = "34.99"
item3_qty = "1"

tax_rate_text = "0.075" # 7.5% sales tax

# conversion
item1_price1 = float(item1_price)
item1_qty1 = int(item1_qty)

item2_price2 = float(item2_price)
item2_qty2 = int(item2_qty)

item3_price3 = float(item3_price)
item3_qty3 = int(item3_qty)

tax_rate = float(tax_rate_text)

subtotal1 = item1_price1 * item1_qty1
subtotal2 = item2_price2 * item2_qty2
subtotal3 = item3_price3 * item3_qty3

Subtotal = subtotal1 + subtotal2 + subtotal3
tax = Subtotal * tax_rate
total = Subtotal + tax


print("=" * 40)
print("STORE RECEIPT")
print("=" * 40)


print(f"Product: {item1_name}")
print(f"Price: ${item1_price1} * {item1_qty1}")
print(f"Subtotal: ${subtotal1:.2f}\n")

print(f"Product: {item2_name}")
print(f"Price: ${item2_price2} * {item2_qty2}")
print(f"Subtotal: ${subtotal2}\n")

print(f"Product: {item3_name}")

print(f"Price: ${item3_price3} * {item3_qty3}")
print(f"Subtotal: ${subtotal3}")

print("-" * 40)

print(f"Subtotal: ${Subtotal}")
print(f"Tax ({tax_rate * 100}%): ${tax:.2f}")

print("=" * 40)

print(f"Total: ${total:.2f}")

print("=" * 40)