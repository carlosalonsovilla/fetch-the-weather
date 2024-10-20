import requests
import os
from dotenv import load_dotenv
import json


load_dotenv()

api_key = os.getenv('API_KEY')

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
        pretty = json.dumps(data, indent=4)
        print(pretty)
    else:
        print(f"Failed to get the weather. Status code: {response.status_code}")

if __name__ == '__main__':
    city = 'St Petersburg,us'
    get_weather(city)