"""
Topic: String Methods and Formatting
"""

# --- upper / lower ---
text = "Python is so easy"
print(text.upper())
print(text.lower())

# --- strip: removes leading/trailing whitespace ---
text = " Python is so easy "
print(text.strip())

# --- replace ---
text = "Python is so easy"
print(text.replace("P", "T"))

# --- split: splits into a list based on a character ---
text = "Python is so, easy"
print(text.split(","))

# --- capitalize: capitalizes only the first letter ---
text = "welcome to my world. How is it going?"
print(text.capitalize())

# --- title: capitalizes the first letter of every word ---
text = "hello i am buse"
print(text.title())

# --- swapcase: swaps upper/lower case ---
text = "Hello I am Buse"
print(text.swapcase())

# --- islower: checks if everything is lowercase ---
text = "which why is it?"
print(text.islower())

# --- String formatting methods ---

# using .format()
age = 24
name = "Buse"
text = "my name is {0}, I am {1}".format(name, age)
print(text)

# using f-string (more practical)
name = "Fehmi Uyar"
age = 34
text = f"My name is {name}, I am {age}"
print(text)

# f-string with decimal precision
price = 19.45468
text = f"The price is {price:.1f} turkish lira"
print(text)
