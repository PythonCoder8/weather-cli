from requests import get
from pprint import pprint

city = input("Which city do you want the weather of?: ")
url = f"https://api.openweathermap.org/data/2.5/weather?units=metric&appid=API_KEY&q={city}"
weather = get(url).json()
if "," in city:
    print(
        f'Currently in {city} it is {round(weather["main"]["temp"])} degrees celsius with a high of {round(weather["main"]["temp_max"])} degrees, and a low of {round(weather["main"]["temp_min"])} degrees. It currently feels like {round(weather["main"]["feels_like"])} degrees.'
    )
else:
    print(
        f'Currently in {city}, {weather["sys"]["country"]} it is {round(weather["main"]["temp"])} degrees celsius with a high of {round(weather["main"]["temp_max"])} degrees, and a low of {round(weather["main"]["temp_min"])} degrees. It currently feels like {round(weather["main"]["feels_like"])} degrees.'
    )
