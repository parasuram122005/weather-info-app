
import json
import urllib.request
import urllib.parse

API_KEY = "your_api_key_here"  # Get free key from openweathermap.org
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def kelvin_to_celsius(k):
    return round(k - 273.15, 1)

def kelvin_to_fahrenheit(k):
    return round((k - 273.15) * 9/5 + 32, 1)

def get_weather(city):
    params = urllib.parse.urlencode({"q": city, "appid": API_KEY})
    url = f"{BASE_URL}?{params}"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
        temp_c = kelvin_to_celsius(data["main"]["temp"])
        temp_f = kelvin_to_fahrenheit(data["main"]["temp"])
        feels_c = kelvin_to_celsius(data["main"]["feels_like"])
        print("\n" + "=" * 29)
        print(f"  Weather in {data['name']}, {data['sys']['country']}")
        print("=" * 29)
        print(f"Condition   : {data['weather'][0]['description'].title()}")
        print(f"Temperature : {temp_c}°C ({temp_f}°F)")
        print(f"Feels Like  : {feels_c}°C")
        print(f"Humidity    : {data['main']['humidity']}%")
        print(f"Wind Speed  : {round(data['wind']['speed']*3.6, 1)} km/h")
        print("=" * 29)
    except Exception as e:
        print(f"Error: Could not fetch weather. Check city name or API key.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
