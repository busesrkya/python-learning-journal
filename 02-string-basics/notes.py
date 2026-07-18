"""
Topic: String Basics - quotes, multiline strings, indexing,
slicing, concatenation, in/not in, escape characters
"""

# --- Using a quote inside a string ---
print("It's alright")
print("He is called \'big boy\'")   # escape character

# --- Multiline string (triple quotes) ---
text = """This is so good
life is good
I'm a variable
"""
print(text)

# --- String indexing and length ---
cars = ["BMW", "Volvo", "Skoda", "Nissan"]
print(cars[0])

text = "Python is easy"
print(len(text))

# --- Using in / not in ---
text = "The best languages in life are free!"
print("expensive" in text)   # False

search = "best"
if search in text:
    print("Yes, 'best' is present")

search = "expensive"
if search not in text:
    print("No, 'expensive' is not present")

# --- String slicing ---
text = "python is weird"
print(text[1:5])
print(text[:5])
print(text[-4:-1])

# --- String concatenation ---
text = "python"
text2 = " is weird"
print(text + text2)

# --- Escape characters ---
print("Python is doing \\ well")   # \\ -> the backslash itself
print("Python\nis\ndoing\nwell")    # \n -> new line
print("Hello\tPyt")                  # \t -> tab space
