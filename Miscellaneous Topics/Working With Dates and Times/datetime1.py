# Create a date object
from datetime import date
date_object = date(2024, 2, 27)
print(date_object)

# Access attributes of the date object
year_from_date=date_object.year 
print(year_from_date)
month_from_date=date_object.month
print(month_from_date)
day_from_date=date_object.day 
print(day_from_date) 

# today()
display_today=date.today()
print(display_today)

# with direct datetime
import datetime
date_object_2=datetime.date(2024,3,3)
print(date_object_2)


