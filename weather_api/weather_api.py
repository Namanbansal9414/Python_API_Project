import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHERAPI_KEY")
BASE_URL = "http://api.weatherapi.com/v1"

def get_current_weather(city):
    url = f"{BASE_URL}/current.json"
    postcode = {"key": API_KEY, "q": city, "aqi": "yes"}

    try:
        response = requests.get(url, params=postcode)
        response.raise_for_status()
        data =  response.json()
    
    except requests.RequestException as e:
        print(f"API request error: {e}")
        return None
    
    if not data:
        print("Failed to retrieve weather.")
        return
    loc = data["location"]
    curr = data["current"]
    location = loc["name"]
    region =loc['region']
    country = loc['country']
    temp_c = curr["temp_c"]
    feelslike_c = curr["feelslike_c"]
    condition = curr["condition"]["text"]
    humidity = curr["humidity"]
    wind_kph = curr["wind_kph"]
    if "air_quality" in curr:
        aq = curr["air_quality"]
        us_epa_index = aq["us-epa-index"]
        pm2_5 = aq["pm2_5"]
    return location, region, country, temp_c, feelslike_c, condition, humidity, wind_kph, us_epa_index, pm2_5
    


def main():
    try:
        city = input("Enter city name: ")
        location, region, country, temp_c, feelslike_c, condition, humidity, wind_kph, us_epa_index, pm2_5 = get_current_weather(city)


        print(f"📍 city : {location}")
        print(f"📍region: {region}")
        print(f"📍country: {country}")
        print(f"🌡 Temperature :{temp_c}°C , (feels like : {feelslike_c}°C)")
        print(f"⚙ Condition : {condition}")
        print(f"💧 Humidity : {humidity}")
        print(f"🌬 Wind : {wind_kph}")
        print(f"🌫 AQI : {us_epa_index} , PM2.5: {pm2_5} μg/m³")
    except Exception as e:
        print(f"An error occurred: {str(e)}")




if __name__ == "__main__":
    main()
