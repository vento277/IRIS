# Function Def'n 
# Collection of all skills into a more executable form.

# Header
import sys
sys.path.append(r"C:\Users\Peter\Desktop\IRIS\components\lib")
import header as h

# Skills
import google_cal as gc
import music as mu
import other as oth
import news as nw
import ordinal as ord
import lights as li
import weather as wth


#------------------------------------------------------Greetings
# Greet according to time
def time_hi():
    currentTime = h.datetime.now()
    currentTime.hour
    morning = h.s.h_morning
    afternoon = h.s.h_afternoon
    night = h.s.h_night

    if currentTime.hour < 12:
        h.ts.tts(h.rd.choice(morning))
    elif 12 <= currentTime.hour < 18:
        h.ts.tts(h.rd.choice(afternoon))
    else:
        h.ts.tts(h.rd.choice(night))


# Farewell according to time
def time_bye():
    currentTime = h.datetime.now()
    currentTime.hour
    before_night = h.s.b_before_night
    night = h.s.b_night

    if currentTime.hour < 12:
       h.ts.tts(h.rd.choice(before_night))
    elif 12 <= currentTime.hour < 18:
       h.ts.tts(h.rd.choice(before_night))
    else:
       h.ts.tts(h.rd.choice(night))

#------------------------------------------------------Schedule
# Return the event in 'text' date of user's google calendar
def calndr(text):
    SERVICE = gc.authenticate_google()
    date = gc.get_date(text)
    gc.get_events(date, SERVICE)

# Ask for a schedule on a particular day of the week.
def calndr_day(text):
    SERVICE = gc.authenticate_google()

    CALENDAR_STRS = ["what do i have", "do i have plans", "am i busy"]

    for phrase in CALENDAR_STRS:
        if phrase in text.lower():
            date = gc.get_date(text)
            if date:
                gc.get_events(date, SERVICE)
            else:
                h.ts.tts("Please Try Again")



#------------------------------------------------------Music
# Turns on music according to the user's request. 
def plymus(user):
    if (h.l.yes(user) == True):
        
        h.ts.tts("which one?")
        choice = h.stt.stt()

        if (mu.music(choice) == True):
            h.ts.tts("here you go")
        else:
            while True:
                h.ts.tts("sorry, I can't find that in your library.")
                choice2 = h.stt.stt()
                mus = mu.music(choice2)
                if (mus == True):
                    h.ts.tts("ah ha, here you go")
                    break
                else:
                    pass

    else:
        h.ts.tts("okay")



#------------------------------------------------------News
# Read out news headlines and open/pass according to user input
def b_news():
    list = nw.news()
    list_pg = nw.page()
    length = len(list)

    for x in range(5):
        h.ts.tts(list[x])

        user = h.stt.stt()

        if (h.l.open(user) == True):
            oth.browser_i(list_pg[x]) 
        else:
            pass

#------------------------------------------------------Project Creation

#------------------------------------------------------Lights
# Configure light
def li_config():
    num_lights = None
    lifx = h.LifxLAN(num_lights)
    devices = lifx.get_lights()

    while True:
        try:
            bulb = devices[0]
            bulb_2 = devices[1]
            print("lightbulbs configured")
            break
        except IndexError:
            print("Having trouble finding your bulbs, please wait...", end="\r")

# Turn on/off lights according to sun-rise and sun-set
def li_time():
    num_lights = None
    lifx = h.LifxLAN(num_lights)
    s = ord.sun(49.246292, -123.116226) 
    sr = int(s[0]) # sunrise
    ss = int(s[1]) # sunset

    ct = ord.time() #current time
    ct_int = int(ct[1])

    if (sr < ct_int < ss):
        lifx.set_power_all_lights("off")
    else:
        lifx.set_power_all_lights("on")

# Turn on/off lights according to user input
def li_onoff(text):
    num_lights = None
    lifx = h.LifxLAN(num_lights)

    if (h.l.light_switch(text) ==  1): 
        lifx.set_power_all_lights("on")

    if (h.l.light_switch(text) == 2):
        lifx.set_power_all_lights("off")

# Change the light according to user input
def li_chg(text):
    num_lights = None
    lifx = h.LifxLAN(num_lights)
    devices = lifx.get_lights()
    bulb_1 = devices[0]
    bulb_2 = devices[1]

    if (h.l.light_types(text) == 1):
        lifx.set_color_all_lights((9284,0,38000,3000)) # House light

    if (h.l.light_types(text) == 2):
        bulb_1.set_color((0, 0, 33000, 5600))
        bulb_2.set_color((7281, 0, 33000, 5600)) # Reading light

    if (h.l.light_types(text) == 3):
        bulb_1.set_color((46602, 23592, 33000, 3500))
        bulb_2.set_color((14381, 3276, 26400, 3500))

    if (h.l.light_types(text) == 4):
        bulb_1.set_color((0, 65535, 33000, 3500))
        bulb_2.set_color((7281, 65535, 33000, 3500))

# Change the brightness according to user input
def li_brghtns(text):
    num_lights = None
    lifx = h.LifxLAN(num_lights)

    if (h.l.light_level(text) == 2 or h.l.no(text) == True):
        init_c = li.color()
        x = init_c[1][0]
        y = init_c[1][1]
        z = init_c[1][3]

        a = init_c[1][2] # current level of brightness
        a -= 1000
        lifx.set_color_all_lights((x,y,a,z))
        h.ts.tts(h.rd.choice(h.s.check))
        light_ctr = h.stt.stt()
        if (h.l.yes(light_ctr) == True):
            pass
        else:
            while True:
                a -= 2000 # dim
                lifx.set_color_all_lights((x,y,a,z))
                h.ts.tts(h.rd.choice(h.s.check))
                light_ctr = h.stt.stt()
                if (h.l.yes(light_ctr) == True):
                    h.ts.tts(h.rd.choice(h.s.okay))
                    break
                else:
                    pass

    if (h.l.light_level(text) == 1):
        init_c = li.color()
        x = init_c[1][0]
        y = init_c[1][1]
        z = init_c[1][3]

        a = init_c[1][2] # current level of brightness
        a += 1000
        lifx.set_color_all_lights((x,y,a,z))
        h.ts.tts(h.rd.choice(h.s.check))
        light_ctr = h.stt.stt()
        if (h.l.yes(light_ctr) == True):
            pass
        else:
            while True:
                a += 2000 # bright
                lifx.set_color_all_lights((x,y,a,z))
                h.ts.tts(h.rd.choice(h.s.check))
                light_ctr = h.stt.stt()
                if (h.l.yes(light_ctr) == True):
                    h.ts.tts(h.rd.choice(h.s.okay))
                    break
                else:
                    pass

# Check the status of the light, and suggest brightness change if needed by the user
def li_check():
    status = li.status()
    if (status == 1):
        h.ts.tts("is the light okay sir?")
        user = h.stt.stt()
        li_brghtns(user)
    else:
        pass