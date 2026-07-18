"""
Topic: Functions - definition, parameters, default values, return, *args, **kwargs
"""

# --- Basic function definition ---
def greet():
    print("Hello!")

greet()
greet()

# --- Function with a parameter ---
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Buse")
greet_person("Ali")

# --- Default parameter value ---
def greet_default(name="Guest"):
    print(f"Hello, {name}!")

greet_default()          # Hello, Guest!
greet_default("Ayse")    # Hello, Ayse!

# --- return: sending a value back from a function ---
def add(a, b):
    return a + b

result = add(3, 5)
print(result)             # 8
print(add(3, 5) * 2)      # 16 -> the returned value can be used in further operations

# --- print vs return ---
def multiply_print(a, b):
    print(a * b)      # only prints to the screen, returns nothing

def multiply_return(a, b):
    return a * b       # returns the value so it can be used elsewhere

x = multiply_print(3, 4)    # prints 12, but x = None!
y = multiply_return(3, 4)   # prints nothing, but y = 12

print(x)   # None
print(y)   # 12

# --- *args: collects positional arguments into a tuple ---
def show_args(*args):
    print(args)
    print(type(args))

show_args(1, 2, 3)

# --- **kwargs: collects keyword arguments into a dictionary ---
def my_name(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print("His lastname is " + kwargs["lastname"])

my_name(firstname="Fehmi", lastname="UYAR")
