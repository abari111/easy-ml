import requests
import pandas as pd

# URL = ("https://api.open-meteo.com/v1/forecast?latitude=48.8534&longitude=2.3488&hourly="
# "temperature_2m,precipitation_probability,snowfall,visibility,wind_speed_10m")

ATTRIBUTES = {'time': 'iso8601', 'temperature_2m': '°C', 'precipitation_probability': '%',
              'snowfall': 'cm', 'visibility': 'm', 'wind_speed_10m': 'km/h'}

def get_url(lat: str, lon: str) -> str:
    url = (f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly="
            "temperature_2m,precipitation_probability,snowfall,visibility,wind_speed_10m")
    return url

def get_hourly_weather_data(lat, lon):
    url = get_url(lat, lon)
    try:
        response = requests.get(url)
        data = response.json()['hourly']
        data = pd.DataFrame(data)
        return data
    except requests.HTTPError as rexp:
        print(rexp)




if __name__ == "__main__":
    data = get_hourly_weather_data(lat=48.8534, lon=2.3488)
    print(data)
