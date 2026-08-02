"""
Topic: math module
The math module provides access to common mathematical functions.
Note: For heavy numerical/array work, NumPy is generally preferred in
data science and AI workflows. This file covers the basics you should
still recognize when reading other people's code.
"""

import math

# --- Constants ---
print("Pi:", math.pi)
print("Euler's number (e):", math.e)

# --- Rounding functions ---
print("Ceiling of 4.2:", math.ceil(4.2))   # rounds up -> 5
print("Floor of 4.8:", math.floor(4.8))    # rounds down -> 4

# --- Power and roots ---
print("Square root of 16:", math.sqrt(16))
print("2 to the power of 5:", math.pow(2, 5))

# --- Logarithms ---
print("Natural log of e:", math.log(math.e))      # base e
print("Log base 10 of 100:", math.log10(100))
print("Log base 2 of 8:", math.log2(8))

# --- Trigonometry (angles in radians) ---
print("Sine of 90 degrees:", math.sin(math.radians(90)))
print("Cosine of 0 degrees:", math.cos(math.radians(0)))

# --- Factorial ---
print("Factorial of 5:", math.factorial(5))

# --- Greatest common divisor ---
print("GCD of 12 and 18:", math.gcd(12, 18))

# --- Distance between two points ---
point_a = (0, 0)
point_b = (3, 4)
distance = math.dist(point_a, point_b)
print("Distance between points:", distance)

# --- isnan / isinf: useful for data cleaning ---
value = float("nan")
print("Is NaN?", math.isnan(value))
print("Is infinite?", math.isinf(float("inf")))
