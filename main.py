import requests
import datetime
from pprint import pprint
from config import weather_token

def get_weather(city,open_weather_token):

    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"


    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric"
        )
        data = r.json()
        #pprint(data)

        city = data["name"]
        cur_weather = data ["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "хз"

        wind = data["wind"]["speed"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        print(f"Погода в {city}\n Температура: {cur_weather} {wd}\n Скорость ветра: {wind}\n Расвет: {sunrise}\n Закат: {sunset}")

    except Exception as ex:
        print(ex)
        print("Ничего не найдено")


def main():
    city = input("Введите город: ")
    get_weather(city, weather_token)

if __name__ == '__main__':
    main()                                                
