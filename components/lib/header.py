import sys
import json
import webbrowser as wb
import random as rd
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from lifxlan import LifxLAN
import pytz
import datetime
from datetime import datetime
from num2words import num2words
from torch import long 
from suntime import Sun, SunTimeException
import time
from playsound import playsound
import requests
import os

sys.path.append(r"C:\Users\Peter\Desktop\IRIS\credentials")
sys.path.append(r"C:\Users\Peter\Desktop\IRIS\components\skills")
sys.path.append(r"C:\Users\Peter\Desktop\IRIS\components\stt")
sys.path.append(r"C:\Users\Peter\Desktop\IRIS\components\tts")
sys.path.append(r"C:\Users\Peter\Desktop\IRIS\components\tts\pyttsx3")

#lib
import listen as l
import speak as s
import playlists as pl

#TTS & STT
import vosk_stt as stt
import azure_tts as tts
import sapi5_tts as ts

