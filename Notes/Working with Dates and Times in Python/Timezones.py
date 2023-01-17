# Import datetime, timedelta, timezone
from datetime import datetime, timedelta, timezone

# Create a timezone for Pacific Standard Time, or UTC-8
pst = timezone(timedelta(hours=-8))

# October 1, 2017 at 15:26:26, UTC-8
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=pst)

# Print results
print(dt.isoformat())

print(dt.astimezone(timezone.utc)) #Print the datetime in UTC

# Create a timezone object corresponding to UTC-4
edt = timezone(timedelta(hours = -4))

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
