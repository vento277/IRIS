# Function Def'n
# Some of the more simpler functions. Often 1 < line of code < 5

# Header
import sys
sys.path.append(r"C:\Users\Peter\Desktop\IRIS\components\lib")
import header as h

# Open browser
def browser(text):
    h.wb.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(h.rd.choice(text))

def browser_i(text):
    h.wb.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(text)

# Random function
def rand(text):
    return h.rd.choice(text)

# Sound
def open():
    h.playsound(r"C:\Users\Peter\Desktop\IRIS\components\sounds\open.mp3")

def wake():
    h.playsound(r"C:\Users\Peter\Desktop\IRIS\components\sounds\wake.mp3")

def done():
    h.playsound(r"C:\Users\Peter\Desktop\IRIS\components\sounds\done.mp3")

def sleep():
    h.playsound(r"C:\Users\Peter\Desktop\IRIS\components\sounds\sleep.mp3")
