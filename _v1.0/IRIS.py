# Personalized AI system: IRIS
# Collection of functions integrated to my life. Only and only function that I require, without any unnecessaries.
# As it's written in python, running the program requires '.bat' file which prevents the script to execute immediately.

# Function modules.
from __future__ import print_function
import sengled
import datetime
import os.path
import requests  
import socket
import os
import sys
import warnings
import calendar
import wikipedia
import random
import pyttsx3
import pygame
import pytz
import pickle
import time
import webbrowser
import socket
import schedule
import json  
import xlwings as xw  
import speech_recognition as sr
import py2exe
from pathlib import Path  
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from SengledElement import client
from playsound import playsound
from lifxlan import LifxLAN, BLUE, CYAN, GREEN,  ORANGE, PINK, PURPLE, RED, YELLOW
from distutils.core import setup

warnings.filterwarnings('ignore')
socket.getaddrinfo('127.0.0.1', 8080) # handle errno11001s

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',' July', 'August', 'September',
                   'October', 'November', 'December']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
DAY_EXTENTIONS = ['st', 'nd', 'rd', 'th']

#------------------------------Functions------------------------------

# Record audio and return it as a string
def recordAudio():

    # record audio
    r = sr.Recognizer() # recognizer object

    # open mic
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 0.5) 
        audio = r.listen(source, phrase_time_limit = 6) # Make sure that the recording dose not exceed the limit of 'google stt'.

    # Google speech Recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said:' + data)
    except sr.UnknownValueError: # except unrecognized speech
        print('Please repeat...', end="\r")

    except sr.RequestError as e:
        print(e) # error such as disconnected ones

    except Exception as e:
        print(e) # except timeout error

    return data

# Get AI response.
def AIresponse(text):
    print(text)

    # convert text -> speech
    converter = pyttsx3.init('sapi5') # initialize 

    voices = converter.getProperty('voices')
    newVoiceRate = 175
    converter.setProperty('rate', newVoiceRate)
    converter.setProperty('voice', voices[1].id)
    converter.say(text) # say the given parameter
    converter.runAndWait() # wait untill all texts are said

# Play random sound in folder (MP3)
def playSound(file_path):
    path = file_path 
    files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.mp3')]
    randomfile = random.choice(files)
    pygame.init()
    pygame.mixer.music.load(randomfile)
    pygame.mixer.music.play()
 
# Verbal cues that returns 'True'
def Wake_word(text):
    WAKE_WORDS = ['iris', 'harris', 'virus', 'hey', 'irish']  # can add as many as you want

    text = text.lower()  # convert to all lower case

    # Check is the users command include a wake phrase
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    return False  

def Power_off(text):
    Off_WORDS = ['shutdown', 'power off']  # can add as many as you want

    text = text.lower()  # convert to all lower case

    # Check is the users command include a wake phrase
    for phrase in Off_WORDS:
        if phrase in text:
            return True

    return False  

def Yes(text):
    Yes_WORDS = ['yes', 'sure', 'sure thing', 'ok', 'okay', 'roger that' , 'yes please']  # can add as many as you want

    text = text.lower()  # convert to all lower case

    # Check is the users command include a wake phrase
    for phrase in Yes_WORDS:
        if phrase in text:
            return True

    return False  

def No(text):
    No_WORDS = ['no', 'nope', 'nah', 'it is fine', 'its fine']  # can add as many as you want

    text = text.lower()  # convert to all lower case

    # Check is the users command include a wake phrase
    for phrase in No_WORDS:
        if phrase in text:
            return True

    return False  

# Greeting by time
def Time_Greet():
    currentTime = datetime.datetime.now()
    currentTime.hour
    morning = ['Good morning', 'Good morning Peter', 'Good morning sir']
    afternoon = ['Good afternoon', 'Good afternoon Peter', 'Good afternoon sir']
    night = ['Good day Peter', 'Good day sir']

    if currentTime.hour < 12:
        AIresponse(random.choice(morning))
    elif 12 <= currentTime.hour < 18:
        AIresponse(random.choice(afternoon))
    else:
        AIresponse(random.choice(night))

def Time_Bye():
    currentTime = datetime.datetime.now()
    currentTime.hour
    before_night = ['Be back soon boss', 'Be back soon boss, you have a game to play', 'Be back soon Peter', 'Be back soon Mr.Kim']
    night = ['Sleep well', 'Sleep well Peter', 'Sleep well Peter. Have a wonderful night', 'Have a wonderful night Peter']

    if currentTime.hour < 12:
       AIresponse(random.choice(before_night))
    elif 12 <= currentTime.hour < 18:
       AIresponse(random.choice(before_night))
    else:
       AIresponse(random.choice(night))

# Google Calendar / Events
def authenticate_google():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    return service

def get_events(day, service): #Get events from google calendar
    date = datetime.datetime.combine(day, datetime.datetime.min.time())
    end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
    utc = pytz.UTC
    date = date.astimezone(utc)
    end_date = end_date.astimezone(utc)

    events_result = service.events().list(calendarId='primary', timeMin=date.isoformat(), timeMax=end_date.isoformat(),
                                        singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        AIresponse('No upcoming events found.')
    else:
        AIresponse(f"You have {len(events)} events on this day.")

        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])
            start_time = str(start.split("T")[1].split("-")[0])
            if int(start_time.split(":")[0]) < 12:
                start_time = start_time + "am"
            else:
                start_time = str(int(start_time.split(":")[0])-12)
                start_time = start_time + "pm"

            AIresponse(event["summary"] + " at " + start_time)

def get_date(text): # Get date from user
    text = text.lower()
    today = datetime.date.today()
    tmr = datetime.date.today() + datetime.timedelta(1)

    if text.count("today") > 0:
        return today
    
    if text.count("tomorrow") > 0:
        return tmr

    day = -1
    day_of_week = -1
    month = -1
    year = today.year

    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(word) + 1
        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENTIONS:
                found = word.find(ext)
                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass

    if month < today.month and month != -1:  
        year = year+1

    
    if month == -1 and day != -1:  
        if day < today.day:
            month = today.month + 1
        else:
            month = today.month

    
    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday()
        dif = day_of_week - current_day_of_week

        if dif < 0:
            dif += 7
            if text.count("next") >= 1:
                dif += 7

        return today + datetime.timedelta(dif)

    if day != -1:  # FIXED FROM VIDEO
        return datetime.date(month=month, day=day, year=year)

# Weather API 
def weather(text):
    # Get value from Name Range
    city_name = text

    # Get City ID
    URL_CITY = f"https://www.metaweather.com/api/location/search/?query={city_name}"
    response_city = requests.request("GET", URL_CITY)
    city_title = json.loads(response_city.text)[0]["title"]
    city_id = json.loads(response_city.text)[0]["woeid"]

    # Get Weather for City ID
    URL_WEATHER = f"https://www.metaweather.com/api/location/{city_id}/"
    response_weather = requests.request("GET", URL_WEATHER)
    weather_data = json.loads(response_weather.text)["consolidated_weather"]

    # Create empty lists
    min_temp = []
    max_temp = []
    weather_state_name = []
    weather_state_abbr = []
    applicable_date = []

    # Iterate over weather_data & append data to lists
    for index, day in enumerate(weather_data):
        min_temp.append(weather_data[index]["min_temp"])
        max_temp.append(weather_data[index]["max_temp"])
        weather_state_name.append(weather_data[index]["weather_state_name"])
        weather_state_abbr.append(weather_data[index]["weather_state_abbr"])
        applicable_date.append(weather_data[index]["applicable_date"])

    print(str(city_title))
    print(str(applicable_date))
    print(str(weather_state_name))
    print(str(max_temp))
    print(str(min_temp))

# Opening websites
def News():
    webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("https://ca.finance.yahoo.com/topic/news") 
    webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pEUVNnQVAB?hl=en-CA&gl=CA&ceid=CA%3Aen")
    
def Music(text):
    if ('morning' in text):
        webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("") 

    if('jazz' in text or 'Jazz' in text):
        webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("") 

# Starting a program
def Program_start():
    os.startfile("C:\Program Files (x86)\Iriun Webcam\webcam.exe")


SERVICE = authenticate_google()
date = get_date('tomorrow')
get_events(date, SERVICE)
AIresponse('Call me if you need anything.')

#------------------------------Functions integrated in convo.------------------------------
# Starting day conversation.   
def start():

    time.sleep(1)
    AIresponse("Welcome to the IRIS station.")
    text = recordAudio()

    while True:
        if(Wake_word(text) == True):
            Time_Greet()

            # Event of the day
            SERVICE = authenticate_google()
            date = get_date('today')
            get_events(date, SERVICE)
            AIresponse('Call me if you need anything.')
            break

        elif('hello again' in text or 'skip' in text):
            Time_Greet()
            break

        else:
            text = recordAudio() 

    os.system('cls')
    print("Getting into background mode...")

# Active functions that I use. 
def active():

    num_lights = None
    SERVICE = authenticate_google()
    lifx = LifxLAN(num_lights)
    devices = lifx.get_lights()
    
    while True:
        try:
            bulb = devices[0]
            bulb_2 = devices[1]
            break
        except IndexError:
            print("Having trouble finding your bulbs, please wait...", end="\r")
            time.sleep(1)
   

    # Scheduling anything needed.
    def job():
        schedule.every().at("16:59").do(lifx.set_power_all_lights("on")) # schedule lightbulb

    while True:

        schedule.run_pending() # execute the scheduled script
        time.sleep(1)

        text = recordAudio() # active listening

        # Shutdown computer. 
        if (Power_off(text) == True):
            AIresponse('In how many minutes?')
            text2 = recordAudio() 

            while True:
                if ('now' in text2):
                    Time_Bye()
                    lifx.set_power_all_lights("off")
                    os.system("shutdown /s /t 1")
                    break
                elif (text2.isdigit()):
                    Time_Bye()
                    shutdown_time = int(text2) * 60
                    os.system("shutdown /s /t" + " " + str(shutdown_time))
                    break
                else: 
                    AIresponse('In how many minutes?')
                    text2 = recordAudio()

        if ("cancel" in text):
                AIresponse('Cancelling the shutdown.')
                os.system("shutdown /a")
 
        # Light bulb control.
        if ("lights on" in text or "I'm home" in text):
            AIresponse("Lights on")
            lifx.set_power_all_lights("on")

        if ("lights off" in text or "I'm going out" in text or "lights out" in text):
            AIresponse("Lights off")
            lifx.set_power_all_lights("off")

        if ("turn down" in text or "dim" in text or "dim lights" in text):
            AIresponse('Turning down the lights')
            lifx.set_color_all_lights((9284,0,20000,3000))

        if ("house lights" in text or "home lights" in text):
            AIresponse('Home lights are on')
            lifx.set_color_all_lights((9284,0,42204,3000))

        if ("bar" in text):
            AIresponse('Bar lights are on')
            bulb.set_color((9284,65535,34668,3500))
            bulb_2.set_color((51335,58981,34733,3500))
            AIresponse("Do you want the music?")
            text_2 = recordAudio()
            if (Yes(text_2) == True): #asks for jazz music
                Music('jazz')
            else:
                AIresponse("Okay")
        
        # Open camera.
        if ('camera' in text):
            Program_start()

        # Music.
        if ('jazz' in text or 'Jazz' in text):
            AIresponse("Enjoy your jazz Peter.")
            Music('jazz')
        if ('morning music' in text):
            AIresponse("Enjoy your music Peter.")
            Music('morning playlist')

        # News.
        if ('news' in text):
           AIresponse("Here is your news.")
           News()

        # Clear Screen.
        if ('clear screen' in text):
            os.system('cls||clear')

        # Exit the program.
        if ('go rest' in text):
            AIresponse("Okay Peter, Relaunch me if you need something.")
            os.system('cls||clear')
            exit()
        
        # Sleep
        if ('sleep' in text):
            AIresponse('for how many minutes?')
            text2 = recordAudio() 

            while True:
                if (text2.isdigit()):
                    sleeptime = int(text2) * 60
                    time.sleep(sleeptime)
                    break
                else: 
                    AIresponse('for how many minutes?')
                    text2 = recordAudio()

        # Perosnal tasks *Must use wake word
        if (Wake_word(text) == True):

            # Event checker.
            CALENDAR_STRS = ["what do i have", "do i have plans", "am i busy"]
            for phrase in CALENDAR_STRS:
                if phrase in text.lower():
                    date = get_date(text)
                    if date:
                        get_events(date, SERVICE)
                       


#------------------------------Main function.------------------------------
def main():

    start()
    active()

if __name__ == "__main__":
    main()
