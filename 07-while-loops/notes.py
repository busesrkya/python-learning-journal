"""
Topic: while Loop, break, continue, else
"""

# --- Basic while ---
i = 1
while i <= 6:
    print(i)
    i += 1

# --- break ---
i = 1
while i <= 6:
    if i == 4:
        break
    print(i)
    i += 1

# --- continue ---
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# --- while...else: runs when the loop finishes normally (no break) ---
i = 1
while i <= 6:
    print(i)
    i += 1
else:
    print("i is now greater than 6")
