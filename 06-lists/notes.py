"""
Topic: Lists - access, modification, methods
"""

cars = ["BMW", "Volvo", "Skoda", "Nissan"]

# --- Access ---
print(cars[0])
print(cars[-1])

# --- Modification ---
cars[1] = "Renault"
print(cars)

# --- Adding items ---
cars.append("Toyota")       # adds to the end
cars.insert(1, "Fiat")      # adds at a specific index
print(cars)

# --- extend: adds items from another list ---
otherCars = ["Mazda", "Honda"]
cars.extend(otherCars)
print(cars)

# --- Removing items ---
cars.remove("Fiat")   # removes by value
print(cars)

del cars[0]            # removes by index
print(cars)

popped = cars.pop()    # removes and returns the last item
print("Removed:", popped)

# --- clear: empties the whole list ---
temp = cars.copy()
temp.clear()
print(temp)

# --- Searching in a list ---
print("Skoda" in cars)

# --- Sorting ---
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
