import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')

city = input("Enter the city you want to check the weather for: ").capitalize()
country = input(f"What country is {city} in? ").upper()

if country == 'US':
    state = input(f"What state is {city} in? (e.g., Florida, New York)? ").capitalize()
    city = f"{city},{state}"

def get_weather(city):
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'imperial'
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        
        if country == 'US':
            print(f"The current temperature in {city}, {country} is {temp}°F")
        else:
            print(f"The current temperature in {city.split(' ,')[0]}, {country.capitalize()} is {temp}°F")

    else:
        print(f"Failed to get the weather. Status code: {response.status_code}")

if __name__ == '__main__':
    get_weather(city)