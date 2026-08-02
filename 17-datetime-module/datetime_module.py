"""
Topic: datetime module
Used for working with dates, times, and date arithmetic.
Very common in real projects: timestamps, logging, deadlines,
data filtering by date range, etc.
"""

from datetime import datetime, date, timedelta

# --- Current date and time ---
now = datetime.now()
print("Current datetime:", now)

today = date.today()
print("Today's date:", today)

# --- Creating a specific date ---
birthday = date(2003, 5, 14)
print("A specific date:", birthday)

# --- Formatting dates (strftime) ---
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted datetime:", formatted)

formatted_date_only = now.strftime("%A, %d %B %Y")
print("Readable date:", formatted_date_only)

# --- Parsing a string into a datetime (strptime) ---
date_string = "02-08-2026"
parsed_date = datetime.strptime(date_string, "%d-%m-%Y")
print("Parsed date:", parsed_date)

# --- Date arithmetic with timedelta ---
one_week_later = today + timedelta(weeks=1)
print("One week from today:", one_week_later)

ten_days_ago = today - timedelta(days=10)
print("Ten days ago:", ten_days_ago)

# --- Difference between two dates ---
start_date = date(2026, 1, 1)
end_date = date(2026, 8, 2)
difference = end_date - start_date
print("Days between start and end:", difference.days)

# --- Comparing dates ---
if end_date > start_date:
    print("End date is after start date")

# --- Practical example: calculate age ---
def calculate_age(birth_date: date) -> int:
    today = date.today()
    age = today.year - birth_date.year
    # subtract 1 if birthday hasn't happened yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

print("Age from birthday example:", calculate_age(birthday))
