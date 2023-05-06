# Function Def'n
# Open certain playlist upon user input

import sys
sys.path.append(r"C:\Users\Peter\Desktop\IRIS\components\lib")
import header as h
import other as oth

# Start music
def music(text):
    if (h.l.music_genre(text) == 1):
        oth.browser(h.pl.morning_list)
        return True

    elif(h.l.music_genre(text) == 2):
        oth.browser(h.pl.jazz_list)
        return True

    elif(h.l.music_artist(text) == 1):
        oth.browser(h.pl.tm_list)
        return True

    else:
        return False

