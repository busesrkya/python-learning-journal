"""
Mini Project: Sort numbers entered by the user
"""

numbers = []
count = int(input("How many numbers will you enter? "))

for i in range(count):
    number = float(input(f"Enter number {i+1}: "))
    numbers.append(number)

numbers.sort()
print("Sorted from smallest to largest:", numbers)

numbers.sort(reverse=True)
print("Sorted from largest to smallest:", numbers)
