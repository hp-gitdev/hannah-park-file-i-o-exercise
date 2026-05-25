
number1 = int(input("Enter number1:"))
print(number1)

try:
   number2 = int(input("Enter number2:"))
except ValueError:
    print("\nThat's not a valid number. Using 0 instead.")
    number2_text = 0

number3 = int(input("Enter number3:"))
print(number3)

sum = number1 + number2_text + number3

numbers = [number1, number2_text, number3]

average = sum/(len(numbers))
print(f"\nYour numbers: {number1}, {number2_text}, {number3}")
print(f"Sum: {sum}")
print(f"Average: {average:.2f} ")