import sys
sys.path.append(r"C:\Users\Peter\Desktop\IRIS\components\skills")
sys.path.append(r"C:\Users\Peter\Desktop\IRIS\components\lib")

import header as h
import brain as br

def start():
    h.os.system("cls")
    print("activted")
    
    user = h.stt.stt()
    wth = br.wth.weather("Vancouver")

    while True:
        if (h.l.wake_word(user) == True):
            br.oth.open()

            # Greet
            br.time_hi() 
            h.ts.tts(
                 "..." + str(br.oth.rand(h.s.welcome))
            )
            h.ts.tts("Today is " + br.ord.mth() + " " + br.ord.day()
            + " " + br.ord.yr() + " ...and the weather is... " + wth[2][0] +
            ", ...the temperature is estimated to be between " + str(int(wth[3][0]))
            + " and " + str(int(wth[4][0])) + " degree celcius."
            )

            # Light
            br.li_config()
            br.li_time()
            br.li_check()

            # News
            h.ts.tts("Here are you news")
            br.b_news()
            h.ts.tts("Alright...")

            # Schedule
            br.calndr("today")

            # Music
            h.ts.tts("Do you want your music?")
            while True:
                mus = h.stt.stt()
                if (h.l.yes(mus) == True):
                    br.plymus(mus)
                    break
                elif(h.l.no(mus) == True):
                    h.ts.tts(br.oth.rand(h.s.okay))
                    break
                else:
                    h.ts.tts("Sorry, I couldn't hear you...")
                    pass

            # Finish
            h.ts.tts("...getting to background mode" + 
                    "...call me if you need anything")

            break

        else:
            user = h.stt.stt()