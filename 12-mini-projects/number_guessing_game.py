"""
Mini Project: Number Guessing Game
The computer picks a random number, the user tries to guess it.
"""

import random

target = random.randint(1, 100)
max_attempts = 7

print("I picked a number between 1 and 100, can you guess it?")

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Guess {attempt}/{max_attempts}: "))

    if guess == target:
        print(f"Congratulations! You guessed it, the number was {target}.")
        break
    elif guess < target:
        print("Try a higher number.")
    else:
        print("Try a lower number.")
else:
    print(f"Out of attempts, the correct number was {target}.")
