item1_name = "Notebook"
item1_price_text = "4.99"
item1_qty_text = "2"

item2_name = "Pen Pack"
item2_price_text = "7.50"
item2_qty_text = "1"

item3_name = "Backpack"
item3_price_text = "34.99"
item3_qty_text = "1"

tax_rate_text = "0.075"   # 7.5% sales tax


item1_price = float(item1_price_text)
item1_qty = int(item1_qty_text)

item2_price = float(item2_price_text)
item2_qty = int(item2_qty_text)

item3_price = float(item3_price_text)
item3_qty = int(item3_qty_text)

item1_total = item1_qty * item1_price
item2_total = item2_qty * item2_price
item3_total = item3_qty * item3_price
subtotal = item1_total + item2_total + item3_total
tax_rate = float(tax_rate_text)
tax = tax_rate * 100 
tax_amount = subtotal * tax_rate
grand_total = subtotal + tax_amount


print("="*45)
print("STORE RECEIPT".center(45))
print ("="*45)

print(f"Notebook    ${item1_price} x {item1_qty}    ${item1_total:.2f}".rjust(40))
print(f"Pen Pack    ${item2_price} x {item2_qty}     ${item2_total:.2f}".rjust(40))
print(f"Backpack    ${item3_price} x {item3_qty}   ${item3_total:.2f}".rjust(40)
      )
print("-"*45)
print(f"Subtotal:                              ${subtotal:.2f}".rjust(40))
print(f"Tax ({tax}%):                             ${tax_amount:.2f}".rjust(40))
print ("="*45)
print(f"TOTAL:                                 ${grand_total:.2f}".rjust(40))
print ("="*45)