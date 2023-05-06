# Function Def'n
# Get the weather using metaweather API

# Header
import sys
sys.path.append(r"C:\Users\Peter\Desktop\IRIS\components\lib")
import header as h

def weather(text):
    # Get value from Name Range
    city_name = text

    # Get City ID
    URL_CITY = f"https://www.metaweather.com/api/location/search/?query={city_name}"
    response_city = h.requests.request("GET", URL_CITY)
    city_title = h.json.loads(response_city.text)[0]["title"]
    city_id = h.json.loads(response_city.text)[0]["woeid"]

    # Get Weather for City ID
    URL_WEATHER = f"https://www.metaweather.com/api/location/{city_id}/"
    response_weather = h.requests.request("GET", URL_WEATHER)
    weather_data = h.json.loads(response_weather.text)["consolidated_weather"]

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

    return city_title, applicable_date, weather_state_name, max_temp, min_temp