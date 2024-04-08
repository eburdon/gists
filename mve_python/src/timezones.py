'''
A python script to remind myself that .now() functions are TZ-naiive; explain the difference between .replace() and .astimezone

NOTE: Really only applies to python 3.8 >= x >= 3.13. datetime.now() was fixed. See:
    DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
'''
import pytz
import datetime

def timezones_example():
    local_tz = 'US/Pacific' # - 07:53
    # local_tz = 'America/Vancouver' # -08:12

    utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
    local_now = datetime.datetime.now().replace(tzinfo=pytz.timezone(local_tz))

    print()
    print(local_tz)
    print()

    print(f'UTC NOW  \t{utc_now.isoformat()}')
    print(f'LOCAL NOW\t{local_now.isoformat()}')
    # UTC NOW   2024-04-08T01:19:38.314922+00:00
    # LOCAL NOW 2024-04-08T01:19:38.314932-07:53
    print("\n")

    print('AS TIMEZONE')
    print(utc_now.astimezone(pytz.timezone(local_tz)).isoformat()) # keeps the timestamp, makes NOT naiive
    print(local_now.astimezone(pytz.timezone(local_tz)).isoformat())
    # 2024-04-07T18:23:17.879759-07:00
    # 2024-04-08T01:23:17.879770-07:53
    print("\n")

    print('REPLACE')
    print(utc_now.replace(tzinfo=pytz.timezone(local_tz)).isoformat()) # has some wierd -07:53 / -08:12
    print(local_now.replace(tzinfo=pytz.timezone(local_tz)).isoformat())
    # 2024-04-08T01:23:17.879759-07:53
    # 2024-04-08T01:23:17.879770-07:53

if __name__ == "__main__":
    timezones_example()
