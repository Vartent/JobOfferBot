import requests
from ..config import OW_API_KEY


# since the API returns degrees in Kelvin, convert them into Celsius
def convert_kel_cel(kel: float):
    return round(kel - 273.15, 1)


# get data about the weather from API
def get_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        reply_message = f"The weather in your location is:\n" \
                        f"Temperature: {convert_kel_cel(float(data['main']['temp']))} °C\n" \
                        f"Clouds: {data['clouds']['all']}%\n"
        return reply_message
    except requests.HTTPError as error:
        print("An error occurred", error)
        return f"An error occurred.\nPlease try again"

# in case user provided his location
def get_weather_by_location(lat: str, lon: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OW_API_KEY}"
    return get_data(url)

# in case user provided city name
def get_weather_by_city(city: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OW_API_KEY}"
    return get_data(url)
