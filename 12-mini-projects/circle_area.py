"""
Mini Project: Calculate the area of a circle
"""

def circle_area(radius):
    pi = 3.14159
    return pi * (radius ** 2)

radius = float(input("Enter the radius of the circle: "))
area = circle_area(radius)
print(f"The area of the circle is: {area:.2f}")
