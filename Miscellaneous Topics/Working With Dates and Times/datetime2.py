# Create a date object
from datetime import time
time_object = time(5, 10, 40)
print(time_object)

# Access attributes of the date object
hour_from_date=time_object.hour
print(hour_from_date)
minutes_from_date=time_object.minute 
print(minutes_from_date)
seconds_from_date=time_object.second 
print(seconds_from_date)
 
# today()


# Get the current time
from datetime import datetime
present_time = datetime.now().time()
print(present_time)


# with direct datetime
import datetime
date_object_2=datetime.date(2024,3,3)
print(date_object_2)

# both date and time at once 
import datetime 
full_date_time_object=datetime.datetime(2024,3,3,7,30,46)
print(full_date_time_object)