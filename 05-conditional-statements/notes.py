"""
Topic: Conditional Statements (if / elif / else)
"""

age = 17
if age < 18:
    print("You are not an adult")
elif age == 18:
    print("Congratulations! You just became an adult")
else:
    print("You are an adult")

# --- Short hand if ---
a = 10
b = 15
print("b is bigger") if b > a else print("a is bigger")

# --- Combined with and / or ---
score = 75
if score < 60:
    print("You failed the exam")
elif score >= 60 and score < 80:
    print("You passed the exam")
else:
    print("You are amazing")
