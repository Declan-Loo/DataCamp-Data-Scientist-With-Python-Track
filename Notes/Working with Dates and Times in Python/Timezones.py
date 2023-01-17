# Import datetime
from datetime import datetime

#Import tz (timezones database)
from dateutil import tz

# Create a timezone object for Eastern Time
et = tz.gettz('America/New_York')

# Create a timezone object for GMT time (London)
uk = tz.gettz('Europe/London')

my_time = datetime(2017,10,12,15,13,20,tzinfo = et)

#Put time in UK timezone.
print(my_time.astimezone(uk))
