"""
Topic: for Loop, range(), usage with tuples/strings, break, continue, else
"""

# --- With a list ---
cars = ["BMW", "Volvo", "Skoda"]
for car in cars:
    print(car)

# --- With a string (character by character) ---
for letter in "Banana":
    print(letter)

# --- With range() ---
for i in range(6):
    print(i)

for i in range(2, 6):
    print(i)

for i in range(2, 30, 3):   # from 2 to 30, step 3
    print(i)

# --- break ---
for car in cars:
    if car == "Skoda":
        break
    print(car)

# --- continue ---
for car in cars:
    if car == "Volvo":
        continue
    print(car)

# --- for...else ---
for i in range(6):
    print(i)
else:
    print("Loop finished (without break)")
