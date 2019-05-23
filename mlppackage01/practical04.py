import datetime
now = datetime.datetime.now()
print("now = ",now)
print(now.year,now.month,now.day,\
      now.hour,now.minute,now.second,now.microsecond)
print(now.strftime("%B "))# B means represents the date and time in string format
print(now.strftime("%b "))

