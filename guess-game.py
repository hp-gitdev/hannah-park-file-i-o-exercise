import random   # built-in module for generating random numbers

play_again = "yes"

while play_again.lower() in ["yes", "y"]:
    secret = random.randint(1,100)  #randint means random integers
    attempts = 0    #this is setting a start
    max_attempts = 7

    print("=== Number Guessing Game ===")
    print("I'm thinking of a number between 1 and 100")
    print(f"You have {max_attempts} attempts.")


    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts+1}/{max_attempts}: "))
        except ValueError:
            print("Please enter valid number.")
            continue

        attempts += 1

        if guess == secret:
            print(f"\nYou got it in {attempts} attempts!")
            break
        elif guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")

        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"{remaining} attems remaining")

    else: print(f"\nOut of attempts! The number was {secret}.")

    play_again = input("\nPlay again? (yes/no): ")

print("Thanks for playing!")