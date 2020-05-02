from datetime import datetime
import pytz


local = datetime.now()
print(local)
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))

# tz_NY = pytz.timezone('America/New_York')
tz_NY = pytz.timezone('Asia/Dhaka')
datetime_NY = datetime.now(tz_NY)
print("Dhaka Time Now:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))