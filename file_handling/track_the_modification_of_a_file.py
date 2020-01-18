import datetime
import time
from datetime import timedelta, date, timezone
from os import path

# Get Time
now_time = datetime.datetime.now()
print("Now It Is ",now_time)

# Get Modifiaction time of a file using Time Module
t = time.ctime(path.getmtime('test.txt'))
print(t)

# Get Modifiaction time of a file using Datetime Module
t = datetime.datetime.fromtimestamp(path.getmtime('test.txt'))
print(t)

# Calculate How many times before a file last modified
last_modified = now_time - t
print("It has been modified: "+ str(last_modified) + " Ago, ",end="")
print("Or " + str(last_modified.total_seconds()) + "Seconds Ago")
