# Guess the Number Game

import random

def guess_the_number():
    number_to_guess = random.randint(1,20)
    attemts = 1
    print("Welcome to the Guess the number game!")
    print("I have selected a number between 1 and 20. Can you guess it?")

    while True:
        guess = int(input("Enter your guess: "))
        if guess < number_to_guess:
            print("Too low! Try again.")
            attemts += 1
        elif guess > number_to_guess:
            print("Too high! Try again.")
            attemts += 1
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attemts} attempts.")
            break

# Example usage
guess_the_number()