destination_text = input("Where is the destination?")
print(f"Destination: {destination_text}")

distance_text = input("What is the toal distance in miles?")
distance = float(distance_text)
print(f"Total Distance: {distance:.2f} miles")

fuel_efficiency_text = input("What is your car's fuel efficiency in miles per gallon?")
fuel_efficiency = float(fuel_efficiency_text)

current_gas_text = input("Waht is the current gas price per gallon?")
current_gas = float(current_gas_text)

gas = fuel_efficiency * current_gas
print(f"Gas ({fuel_efficiency:.2f}gallon @ ${current_gas:.2f}/gal): ${gas:.2f}")

hotel_text = input("How many nights are you staying at the hotel?")
hotel = int(hotel_text)

hotel_price_text = input("What is the average hotel cost per night?")
hotel_price = float(hotel_price_text)

hotel_total = hotel * hotel_price
print(f"Hotel ({hotel} nights @ ${hotel_price:.2f}): ${hotel_total:.2f})")

daily_budget_text = input("What is the daily food budget?")
daily_budget = float(daily_budget_text)
daily_total = (hotel+1) * daily_budget
print(f"Food ({hotel+1} days @ ${daily_budget:.2f}): ${daily_total:.2f}")

Total = gas + hotel_total + daily_total
print(f"Estimated Total: ${Total:.2f}")
