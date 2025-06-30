import random

print(" Welcome to the Number Guessing Game!")

while True:
    number = random.randint(1, 100)
    attempts = 0
    print("\nI'm thinking of a number between 1 and 100.")

    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f" Correct! You guessed it in {attempts} attempts.")
            break

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! ")
        break
