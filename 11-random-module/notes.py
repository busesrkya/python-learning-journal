"""
Topic: the random module
"""

import random

# --- Random integer (both endpoints inclusive) ---
number = random.randint(1, 10)
print(number)

# --- Random float between 0.0 and 1.0 ---
decimal = random.random()
print(decimal)

# --- Picking a random item from a list ---
fruits = ["apple", "pear", "banana", "strawberry"]
chosen = random.choice(fruits)
print(chosen)

# --- Shuffling a list ---
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print(cards)

# --- Picking multiple random items (without repetition) ---
selection = random.sample(fruits, 2)
print(selection)
