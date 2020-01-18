from datetime import datetime, date

# Today's Date and Time
now_time = datetime.now()
print("Now It Is ", now_time)

# Today's Time
todays_time = datetime.time(datetime.now())
print(todays_time)

# Today's Date
today = date.today()
print("Today's Date", today)

# Date Components
print("Today is: {}-{}-{}".format(today.day, today.month, today.year))

# Retrieve Weekday
# Note: Python weekday starts from Monday
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print("Today's Weekday is:", days[today.weekday()])
