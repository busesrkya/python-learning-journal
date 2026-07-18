"""
Topic: List Comprehension
Goal: writing loop-based list creation in a single line
"""

# --- The classic way (with for) ---
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

# --- The same result with list comprehension ---
newlist = [x for x in fruits if "a" in x]
print(newlist)

# --- Example with numbers: squares from 1 to 10 ---
squares = [x**2 for x in range(1, 11)]
print(squares)

# --- Conditional list comprehension: only even numbers ---
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)

# --- List comprehension with if/else ---
numbers = [1, 2, 3, 4, 5]
result = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(result)
