"""
Topic: Arithmetic, Comparison, Logical and Identity Operators
"""

# --- Arithmetic operators ---
number1 = 12
number2 = 7

print(number1 + number2)     # addition
print(number1 ** number2)    # exponent
print(number1 % number2)     # modulus (remainder)
print(number1 // number2)    # floor division

# --- Comparison operator example ---
realPassword = "12345"
myPassword = "12345"   # normally taken via input()

if realPassword == myPassword:
    print("Congratulations, it's the correct password")
else:
    print("Sorry, that is the wrong password")

# --- Logical operator: and ---
score = 75
if score < 60:
    print("You failed the exam")
elif score >= 60 and score < 80:
    print("You passed the exam")
else:
    print("You are amazing")

# --- Logical operator: or ---
score = 95
if score < 10 or score >= 90:
    print("You are amazing")
elif score >= 10 and score < 50:
    print("You failed the exam")
else:
    print("You passed the exam")

# --- Logical operator: not ---
score = 40
if not (score > 50):
    print("You failed the exam")
else:
    print("You passed the exam")

# --- Identity operators: is / is not ---
# having the same VALUE is different from being the same OBJECT!
x = ["strawberry", "grape", "pineapple"]
y = ["strawberry", "grape", "pineapple"]
z = x   # z points to the same object as x

print(x is y)    # False -> equal values, but different objects
print(x is z)    # True  -> they point to the same object
print(x == y)    # True  -> equal in value

print(x is not y)   # True
