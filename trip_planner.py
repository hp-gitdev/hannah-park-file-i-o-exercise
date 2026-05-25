
print("===", "Road Budge Planner", "===")

destination = input("What is your Destination?")
print(f"Detination: {destination}")

distance_text = input("What is the total distance in miles?")
distance = float(distance_text)
print(f"Distance: {distance:.2f} miles")

print("---", "Cost Breakdown", "---")

fuel_efficiency_text = input("What is your car's fuel efficiency in miles per gallon?")
fuel_efficiency = float(fuel_efficiency_text)
print(f"Fuel efficienty: {fuel_efficiency:.2f}")
gas_cost_text = input("What is the current gas price per gallon?")
gas_cost = float(gas_cost_text)
gas_total = fuel_efficiency * gas_cost
print(f"Gas ({fuel_efficiency:.2f}gal @ ${gas_cost:.2f}/gal): ${gas_total:.2f} ")

stay_text = input("How many nights are you staying?")
stay = int(stay_text)
hotel_cost_text = input("How much is the average hotal cost per night?")
hotel_cost = float(hotel_cost_text)
hotel_total = stay * hotel_cost
print(f"Hotel ({stay}nights @ ${hotel_cost:.2f}): ${hotel_total:.2f}")

food_budget_text = input("How much will you spend on food daily?")
food_budget = float(food_budget_text)
food_total = stay * food_budget
print(f"Food ({stay}days @ ${food_budget:.2f}): ${food_total:.2f}")

print("-" *40)

total = gas_total + hotel_total + food_total
print(f"Estimated Total: ${total:.2f}")