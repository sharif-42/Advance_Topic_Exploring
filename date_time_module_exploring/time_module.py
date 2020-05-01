from datetime import time

time_info = time(11, 34, 56)
time_info = "Hours:{}, Minute:{}, Second:{}, microsecond:{}"\
    .format(time_info.hour, time_info.minute, time_info.second, time_info.microsecond)
print(time_info)