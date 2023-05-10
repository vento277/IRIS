# Purpose:
# - Retrive data from openweathermap.com
# - Compare forecasted-data from current-data and return % difference for conversation purpose
# - Send sunrise and sunset data for lighting control

#https://api.openweathermap.org/data/2.5/onecall?lat=48&lon=-123&appid=42b362bd537f39b118691891848a093e&units=metric%20%%20(lat,%20lon,%20api_key)

# Header
import requests
import json

# Class for extracting the needed data from openweathermap
# 1. get_data(self): returns temperature, humidity, and wind speed data
# 2. compare_data(self): returns the % difference of the today_temp to tmr_temp
class Weather:

    def __init__(self, key, lat, lon):
        self.key = key
        self.lat = lat
        self.lon = lon


    def get_data(self):
        url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (self.lat, self.lon, self.key)
        response = requests.get(url)
        data = json.loads(response.text)

        curr_temp = data['current']['temp']
        curr_fl = data['current']['feels_like']
        curr_wind = data['current']['wind_speed']
        curr_wth = data['current']['weather'][0]['description']

        fore_temp_morn = data['daily'][2]['temp']['morn']

        print(curr_temp, curr_fl, curr_wind, curr_wth)
        print(fore_temp_morn)

        # return temp2, hmd2, wind2["speed"]

    def compare_data(self):
        pass

    
w = Weather('', '48.208176','-123')
w.get_data()






