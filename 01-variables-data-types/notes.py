"""
Topic: Variables and Data Types
"""

# --- Variable assignment ---
x = 7
y = "python"
print(x)
print(y)

# --- Checking data type with type() ---
print(type(x))   # <class 'int'>
print(type(y))   # <class 'str'>

# --- Single or double quotes both work ---
z = 'awesome'
print(z)

# --- Variable naming rules ---
_name = "Buse"
name = "Buse"
name2 = "Emre"
Myname = "Eylem"

# --- Multi-word variable names (camelCase / snake_case) ---
totalCubeVolume = 70
triangleArea = 90
total_cube_volume = 95

# --- Assigning values to multiple variables in one line ---
x, y, z = "Banana", "Apple", "Grape"
print(x, y, z)

a = b = c = "red"   # same value assigned to all three
print(a, b, c)

# --- Printing multiple variables at once ---
x = "Python"
y = "is"
z = "wonderful"
print(x, y, z)

# --- Numeric and other data types ---
name = "Fehmi"      # string
age = 34            # integer
weight = 84.15       # float
complexNum = 2j       # complex

print("name:" + name + " age:" + str(age) + " weight:" + str(weight))
print(type(name), type(age), type(weight))

# --- list, range, dict, set data types ---
myList = ["Apple", "Grape", "Cherry", "Watermelon", "Lemon", "Banana"]
print(type(myList))
print(myList)

myRange = range(9)
print(*myRange)         # * unpacks and prints all elements separately

myDict = {"name": "Fehmi", "age": 34}
print(myDict)

mySet = {"Apple", "Grape", "Cherry", "Watermelon"}
print(mySet)
