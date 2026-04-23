# Weather Info App

A Python command-line application that fetches real-time weather data for any city worldwide.

## Features
- Get current temperature, humidity, wind speed
- Display weather conditions (sunny, cloudy, rainy, etc.)
- Support for any city in the world
- Clean formatted output
- Error handling for invalid cities

## Setup
```bash
pip install requests
```

Get a free API key from: https://openweathermap.org/api

## How to Run
```bash
python weather_app.py
```

## Example Output
```
=============================
  Weather in Chennai, IN
=============================
Condition   : Partly Cloudy
Temperature : 32°C (89°F)
Feels Like  : 36°C
Humidity    : 74%
Wind Speed  : 18 km/h
=============================
```

## Tech Stack
- Python 3
- requests library
- OpenWeatherMap API (free tier)
