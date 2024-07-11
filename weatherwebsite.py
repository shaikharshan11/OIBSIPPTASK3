import streamlit as st
import requests
import json

API_KEY = "cb55d9dbfcb42cd5c8065112d582ba83"

def get_weather_data(location):

  url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
  response = requests.get(url)

  if response.status_code == 200:
    return response.json()
  else:
    st.error(f"Error: {response.status_code}")
    return None

def display_weather(data):
  
  city = data["name"]
  temp = data["main"]["temp"]
  humidity = data["main"]["humidity"]
  weather_desc = data["weather"][0]["description"]
  icon_code = data["weather"][0]["icon"]

  icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
  st.image(icon_url, width=100)

  st.write(f"## Location: {city}")
  st.write(f"**Temperature:** {temp:.2f} °C")
  st.write(f"**Humidity:** {humidity}%")
  st.write(f"**Weather:** {weather_desc}")

def main():
  st.title("Weather Website by Mohammad Arshan Shaikh")
  
  location = st.text_input("Enter city or ZIP code:")

  if location:
    weather_data = get_weather_data(location)
    if weather_data:
      display_weather(weather_data)
    else:
      st.warning("Failed to retrieve weather data. Please check location or API key.")

if __name__ == "__main__":
  main()
