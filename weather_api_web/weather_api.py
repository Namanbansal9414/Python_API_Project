
import requests
import streamlit as st

API_KEY = "1e9fc4ace0e149d6bb2133632251307"
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
        
    
    if not data:
        print("Failed to retrieve weather.")
        return
    else:
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
    
    
st.set_page_config(page_title="🌤 Weather App", layout="centered")
st.title("🌤 Live Weather App")
st.subheader("Enter a city to get current weather info")

city = st.text_input("**Enter The City Name**" , placeholder="e.g. New York, London, Tokyo")

def main():
    try:
        location, region, country, temp_c, feelslike_c, condition, humidity, wind_kph, us_epa_index, pm2_5 = get_current_weather(city)

        st.success(f"Weather in {location}, {region}, {country}")
        st.write(f"🌡 **Temperature** : {temp_c}°C , (Feels like : {feelslike_c}°C)")
        st.write(f"⚙ **Condition** : {condition}")
        st.write(f"💧 **Humidity** : {humidity}%")
        st.write(f"🌬 **Wind** : {wind_kph} kph")
        st.write(f"🌫 **AQI** : {us_epa_index} | **PM2.5** : {pm2_5} μg/m³")
    except Exception as e:
        st.error(f"Could not fetch weather data: {e}")


if __name__ == "__main__":
    main()
