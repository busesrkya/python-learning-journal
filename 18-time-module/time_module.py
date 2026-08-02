"""
Topic: time module
Lower-level module for working with time, mainly used for measuring
execution time, adding delays, and getting raw timestamps.
Different from datetime: time deals more with "system clock" style
operations rather than calendar dates.
"""

import time

# --- Current time as a Unix timestamp (seconds since 1970) ---
timestamp = time.time()
print("Current timestamp:", timestamp)

# --- Converting a timestamp to a readable structure ---
local_time = time.localtime(timestamp)
print("Local time struct:", local_time)

readable_time = time.strftime("%d-%m-%Y %H:%M:%S", local_time)
print("Readable local time:", readable_time)

# --- Measuring how long code takes to run ---
start = time.time()

total = 0
for i in range(1_000_000):
    total += i

end = time.time()
print(f"Loop took {end - start:.4f} seconds")

# --- time.perf_counter(): more precise for benchmarking ---
start_perf = time.perf_counter()
total = sum(range(1_000_000))
end_perf = time.perf_counter()
print(f"Loop with perf_counter took {end_perf - start_perf:.6f} seconds")

# --- Adding a delay (use carefully, mostly for demos/scripts) ---
print("Waiting 1 second...")
time.sleep(1)
print("Done waiting.")
