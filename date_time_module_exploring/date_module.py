from datetime import datetime, date

"""
# Create a date
Here date() is a constructor of the date class. 
The constructor takes three arguments: year, month and day.
"""
d = date(2020, 5, 1)
print(d)

# Get current date
today = date.today()
print("Current date :", today)

# Get date from a timestamp
timestamp = date.fromtimestamp(1590244364)
print("Date =", timestamp)

# Today's Months , Day
today = date.today()
to_day = "Current Year:{}, Month:{}, " \
         "Day:{}".format(today.year, today.month, today.day)
print(to_day)


