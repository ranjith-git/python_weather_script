from urllib.request import urlopen
import urllib.error
import json
import datetime as dt
import pytz
city_name = input('City: ')
YOUR_APP_ID = "90768b2590dceed79369f286990fae0c"
try:

    with urlopen(
        f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={YOUR_APP_ID}"
    ) as res:
        json_data = res.read()

    read_json = json.loads(json_data)
except urllib.error.HTTPError:
    print(f'Invalid input:{city_name}')
    exit()

def time_stamp(time):
    return dt.datetime.fromtimestamp(time).time()

  
sunrise_time = time_stamp(read_json["sys"]["sunrise"])
sunset_time = time_stamp(read_json["sys"]["sunset"])

print(f"longitude: {read_json['coord']['lon']}, latitude: {read_json['coord']['lat']}, country: {read_json['sys']['country']}")
print(f"Sunrise Time: {sunrise_time}")
print(f"Sunset Time: {sunset_time}")
print(f"Temperature: {read_json['main']['temp']}°C")
print(
    f"Clouds: {read_json['clouds']['all']}%, {read_json['main']['pressure']} hPa"
)
print(f"Humidity: {read_json['main']['humidity']}%")
print(f"Wind: {read_json['wind']['speed']} m/s")
print(
    f"Weather: {read_json['weather'][0]['main']}({read_json['weather'][0]['description']})"
)
