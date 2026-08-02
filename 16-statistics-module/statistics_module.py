"""
Topic: statistics module
Built-in module for basic descriptive statistics on numeric data.
Relevant for data science: this is the lightweight version of what
Pandas/NumPy do at scale, but good to know for small datasets and
quick calculations without extra dependencies.
"""

import statistics

data = [12, 15, 12, 18, 20, 15, 15, 22, 30]

# --- Measures of central tendency ---
print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))          # most frequent value

# --- Measures of spread ---
print("Variance:", statistics.variance(data))          # sample variance
print("Standard deviation:", statistics.stdev(data))    # sample stdev
print("Population variance:", statistics.pvariance(data))
print("Population stdev:", statistics.pstdev(data))

# --- Quantiles ---
quartiles = statistics.quantiles(data, n=4)
print("Quartiles (Q1, Q2, Q3):", quartiles)

# --- Working with grades example ---
grades = [65, 70, 85, 90, 92, 78, 88]
print("\nGrades example:")
print("Average grade:", statistics.mean(grades))
print("Median grade:", statistics.median(grades))
print("Grade standard deviation:", round(statistics.stdev(grades), 2))

# --- Harmonic and geometric mean (less common but useful to know) ---
positive_values = [10, 20, 40]
print("\nGeometric mean:", statistics.geometric_mean(positive_values))
print("Harmonic mean:", statistics.harmonic_mean(positive_values))
