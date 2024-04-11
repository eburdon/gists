'''
A python script to remind myself that .now() functions are TZ-naiive; explain the difference between .replace() and .astimezone
'''
import pytz # this is also deprecated; use stdlib (below)
from datetime import datetime, timezone

def timezones_example():
    print_counter = 0

    # inner function
    def print_timevalue(value: datetime):
        nonlocal print_counter
        value = value.replace(microsecond=0)
        print(f"({print_counter})", value.isoformat())
        print_counter += 1

    ########
    # The deprecated `utcnow` AND new now() function
    # both create TZ-naiive objects!

    deprecated_utc_now = datetime.utcnow()
    print_timevalue(deprecated_utc_now)

    # now(): If optional argument tz is None or not specified, this is like today().
    #   Return the current local datetime.
    new_utc_now = datetime.now()
    print_timevalue(new_utc_now)

    ## (0) 2024-04-10T05:13:21 # deprecated; correct hour, not TZ-aware
    ## (1) 2024-04-09T22:13:21 # system time!!

    ########
    ## Create TZ-aware objects for UTC

    # previous way
    deprecated_utc_now_with_tz = datetime.utcnow().replace(tzinfo=pytz.UTC)
    print_timevalue(deprecated_utc_now_with_tz)

    # style advised in the deprecation notice
    now_with_stdlib_tz = datetime.now(timezone.utc)
    print_timevalue(now_with_stdlib_tz)

    # could also use pytz (oslo TZ)
    # no benefits to using this lib anymore; use stdlib (datetime.timezone)
    now_with_pytz_tz = datetime.now(pytz.UTC)
    print_timevalue(now_with_pytz_tz)

    # WARNING: don't just `replace` the timezone...
    now_with_replace_stdlib = datetime.now().replace(tzinfo=timezone.utc)
    print_timevalue(now_with_replace_stdlib)

    # these are all correct...
    ## (2) 2024-04-10T05:13:21+00:00 
    ## (3) 2024-04-10T05:13:21+00:00 # advised way
    ## (4) 2024-04-10T05:13:21+00:00
    
    ## (5) 2024-04-09T22:13:21+00:00 # incorrect!

    ########
    # If you merely want to attach a time zone object tz to a datetime dt WITHOUT ADJUSTMENT
    #   of date and time data, use dt.replace(tzinfo=tz). 
    # Otherwise, `astimezone`:
    #   Return a datetime object with new tzinfo attribute tz, adjusting the date and time data
    #   so the result is the same UTC time as self, but in tz’s local time.

    # convert UTC time to target TZ: PST

    utc_now = datetime.now(timezone.utc)
    utc_now_naiive = datetime.now()
    local_tz = 'US/Pacific' # 'America/Vancouver'

    # TODO: replace pytz.
    #    tz must be an instance of a tzinfo subclass.
    utc_as_pst = utc_now.astimezone(pytz.timezone(local_tz)) # cannot take string value; pass in PYTZ
    print_timevalue(utc_as_pst)

    # Changed in version 3.6: The astimezone() method can now be called on naive instances that are
    # presumed to represent system local time.
    utc_naiive_as_pst = utc_now_naiive.astimezone(pytz.timezone(local_tz))
    print_timevalue(utc_naiive_as_pst)

    # these are correct. Different hour than UTC with appropriate TZ offset
    # can use either TZ-aware or naiive object
    ## (6) 2024-04-09T22:13:21-07:00
    ## (7) 2024-04-09T22:13:21-07:00

    ########
    # What about `localize`? PYTZ specific?

    # NOTE: can't call localize on a TZ-aware datetime
    # pytz.timezone(local_tz).localize(utc_now)

    beta = pytz.timezone(local_tz).localize(utc_now_naiive)
    print_timevalue(beta)
    
    # also correct
    ## (8) 2024-04-09T22:13:21-07:00

    charlie = pytz.UTC.localize(utc_now_naiive)
    print_timevalue(charlie)

    # wrong; this is the system time (PST hour) with a UTC timestamp
    ## (9) 2024-04-09T22:13:21+00:00

if __name__ == "__main__":
    timezones_example()
