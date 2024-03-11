from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Des Moines"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={
        os.getenv("API_KEY")}&q={city}&units=imperial'
    # pasted url from the lesson 21
    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')
    city = input("\nPlease enter a city name: ")


# check for empty strings or strings with only spaces
    if not bool(city.strip()):
        city = "Des Moines"
# when i ran this file, you initially get an error. fix this by control + c a few times, and then run python file again. get prompt in terminal to enter a city name, i hit enter and it will return the weather for des moines. same case for empty spaces
    # if user doesnt input a city it will default to Des Moines
    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)
# create server.py now and implement flask
