"""
Topic: Dictionaries - access, adding, removing, iterating, reference vs copy
"""

person = {"name": "Seyda", "age": 36, "country": "Turkiye"}

# --- Access ---
print(person["name"])
print(person.get("age"))   # .get() is safer: returns None instead of an error if the key is missing

# --- Updating / Adding ---
person["age"] = 37
person.update({"city": "Istanbul", "job": "Engineer"})
print(person)

# --- Removing ---
removed = person.pop("job")
print("Removed:", removed)
del person["city"]
print(person)

# --- Iterating ---
for key in person:
    print(key)

for key, value in person.items():
    print(f"{key}: {value}")

# --- IMPORTANT: = shares a reference, it does not copy ---
car = {"brand": "Skoda", "year": 1939}
car2 = car              # car2 refers to the same dictionary
car["year"] = 2009
print(car2)               # year: 2009 -> car2 changed too!

# --- copy() is required for an independent copy ---
car = {"brand": "Skoda", "year": 1939}
car2 = car.copy()
car["year"] = 2009
print(car2)                # year: 1939 -> car2 was NOT affected
