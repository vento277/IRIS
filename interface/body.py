# Body of iris, including program exit

# Header
import sys
sys.path.append(r"C:\Users\Peter\Desktop\IRIS\components\skills")
sys.path.append(r"C:\Users\Peter\Desktop\IRIS\components\lib")

import header as h
import brain as br

def functions(text):

    # Thank
    if (h.l.thank(text) == True):
        h.ts.tts(br.oth.rand(h.s.welc))

    # Calendar
    if (h.l.check_events(text) == True):
        br.calndr_day(text)

    # Music
    if (h.l.music(text) == True):
        br.plymus('yes')

    # Lights
    if (h.l.light_switch(text) != 0):
        br.li_onoff(text)
    if (h.l.light_types(text) != 0):
        br.li_chg(text)
    if (h.l.light_level(text) != 0):
        br.li_brghtns(text)

    #Setting up workstations for projects (automate work stations)



def body():
    h.os.system("cls")
    print("running...")
    while True:
        user = h.stt.stt()

        if (h.l.wake_word(user) == True):
            br.oth.wake()

            while True:
                user2 = h.stt.stt()
                functions(user2)

        else:
            h.os.system("cls")
            pass
    

       
      
