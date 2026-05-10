# PART 1: Error Detective

# snippet 1 
# predicting a typeError, and the error msg will say "can only concatenate str (not "int") to str"
#The actual error: typeError
#Fix below:

answer = int(input("Enter your answer:"))
print(f"The answer is: {answer} + 42")


#snippet 2
#predicting a typeError, and the error msg will say "can only concatenate str (not "int") to str"
#The actual error: typeError
#fix below:

favorite = int(input("Favorite number:"))
result = favorite + 10
print(result)


#snippet 3
#predicting: syntaxError, and the error msg will say "unterminated string literal"
#The actual error: syntaxError
#fix below:

print("Hello World")


#snippet 4
#predicting: valueError, and the error msg wil say "invalid literal for int() with base 10: 'twenty-five'"
#The actual error: valueError
#fix below:

age = int(25)
print(f"{age}")


#snippet 5
#predicting: nameError, and the error msg will say "name 'username' is not defined"
#The actual error: nameError
#fix below:

username = input("cool guy")
print(f"{username}")




#Part 2: Crash-Proof Number Collector

try:
    number_1 = int(input("Enter your first number: "))

except ValueError:
    print("\nError. That's not a valid number. Using 0 instead")
    number1 = int(0)
    print(f"Enter number 1: {number1}")

try:
    number_2 = int(input("Enter your second number: "))

except ValueError:
    print("\nError. Please enter a numeric number. (e.g. 2)")
    number2 = int(input("Enter your second number: "))
    print(f"Enter number 2: {number2}")

 
    number3 = int(input("Enter your third number: "))
    print(f"Enter number 3: {number3}")

print(f"Your numbers: {number1}, {number2}, {number3}")
sum = number1 + number2 + number3
print(f"Sum: {sum}")
average = number1 + number2 + number3 / 3
print(f"Average: {average:.2f}")
