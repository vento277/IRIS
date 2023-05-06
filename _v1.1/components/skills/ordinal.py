# Function Def'n
# Return dates in the ordinal strings

# Header
import sys
sys.path.append(r"C:\Users\Peter\Desktop\IRIS\components\lib")
import header as h

def day():
    date_time = h.datetime.today()

    a = date_time.strftime("%d")
    a = int(a)
    a = h.num2words(a, to ="ordinal")
    return a

def mth():
    date_time = h.datetime.today()

    a = date_time.strftime("%b")
    return a

def yr():
    date_time = h.datetime.today()

    a = date_time.strftime("%Y")
    a = int(a)
    a = h.num2words(a, to ="year")
    return a

def mth_yr_display():
    date_time = h.datetime.today()

    a = date_time.strftime("%m/%d/%Y, %H:%M:%S")
    return a

def time():
    date_time = h.datetime.today()

    a = date_time.strftime("%H %M %p")
    b = date_time.strftime("%H%M")
    return a, b

def sun(latitude, longitude):
    sun = h.Sun(latitude, longitude)

    today_sr = sun.get_sunrise_time()
    today_ss = sun.get_sunset_time()
    tz_van = h.pytz.timezone('Canada/Pacific')

    sr = today_sr.astimezone(tz_van).strftime('%H%M')
    ss = today_ss.astimezone(tz_van).strftime('%H%M')
    return sr, ss