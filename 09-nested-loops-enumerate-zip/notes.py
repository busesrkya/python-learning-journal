"""
Topic: Nested Loops, enumerate(), zip()
"""

# --- Nested loop ---
adjectives = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for a in adjectives:
    for f in fruits:
        print(a, f)

# --- Iterating over a nested list ---
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for num in row:
        print(num, end=" ")
    print()

# --- enumerate: gives both index and value at the same time ---
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# --- zip: lets you iterate over two lists at the same time ---
names = ["Ali", "Ayse", "Mehmet"]
ages = [25, 30, 22]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
