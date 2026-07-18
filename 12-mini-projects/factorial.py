"""
Mini Project: Calculate the factorial of a number
Example: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""

number = int(input("Enter the number to calculate its factorial: "))
result = 1

for i in range(1, number + 1):
    result *= i

print(f"{number}! = {result}")
