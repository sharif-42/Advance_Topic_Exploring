from datetime import datetime, date, timedelta

"""
The way date and time is represented may be different in different places, 
organizations etc. It's more common to use mm/dd/yyyy in the US, 
whereas dd/mm/yyyy is more common in the UK.
"""

# strftime()
"""
The strftime() method is defined under classes date, datetime and time. 
The method creates a formatted string from a given date, datetime or 
time object.
"""
now = datetime.now()
print(now)
t = now.strftime("%H/%M/%S")
print("time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
print(s1)
"""
Here, %Y, %m, %d, %H etc. are format codes. The strftime() method 
takes one or more format codes and returns a formatted string
based on it.

In the above program, t, s1 and s2 are strings.
    %Y - year [0001,..., 2018, 2019,..., 9999]
    %m - month [01, 02, ..., 11, 12]
    %d - day [01, 02, ..., 30, 31]
    %H - hour [00, 01, ..., 22, 23
    %M - minute [00, 01, ..., 58, 59]
    %S - second [00, 01, ..., 58, 59]
"""

# strptime()
"""
The strptime() method creates a datetime object from a given 
string (representing date and time).
"""
date_string = "2 May, 2020"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
"""
The strptime() method takes two arguments:
    1. a string representing date and time
    2. format code equivalent to the first argument

By the way, 
%d, %B and %Y format codes are used for day, month(full name) and year.
"""