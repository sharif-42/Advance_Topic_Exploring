from datetime import datetime, date, timedelta

# Today's Date and Time
now_time = datetime.now()
print("Now It Is ", now_time)

# Today's Time
todays_time = datetime.time(datetime.now())
print("Today is", todays_time)

# Today's Date
today = date.today()
print("Today's Date", today)

# Date Components
print("Today is: {}-{}-{}".format(today.day, today.month, today.year))

# Retrieve Weekday
# Note: Python weekday starts from Monday
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print("Today's Weekday is:", days[today.weekday()])


# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(b)

# Timestamp of a datetime
print("Time Stamp :",b.timestamp())

# Difference between two date and time
t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)

t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)

