# Weather Fetcher

A simple Python script that fetches weather information for **St. Petersburg, FL** using the OpenWeatherMap API.

## Current Features
- Fetches the temperature and weather condition for St. Petersburg, FL.

## Future Plans
- Make the script dynamic to allow users to input the city they want to check.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/carlosalonsovilla/fetch-the-weather.git
   cd fetch-the-weather
   ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    .\venv\Scripts\activate  # On Windows
    ```
3. Create a .env file in the project root and add your OpenWeatherMap API key:
    ```
    API_KEY=your_api_key_here
    ```

## Usage

1. Run the script to fetch the weather information:
    ```bash
    python check_the_weather.py
    ```



