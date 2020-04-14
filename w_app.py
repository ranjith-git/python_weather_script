from urllib.request import urlopen
import json
import datetime as dt
import re
import pytz

lat, lon, c_code, c_name = None, None, None, input("Country: ")
YOUR_APP_ID = "90768b2590dceed79369f286990fae0c"

with open("country_info.json") as rf:
    contry_info = json.load(rf)
for x in contry_info:
    if x["name"].casefold() == c_name.casefold():
        lat = x["latitude"]
        lon = x["longitude"]
        c_code = x["country"]
        break
if lat == None:
    print(f"Invalid input:{c_name}")
    exit()

with urlopen(
    f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&appid={YOUR_APP_ID}"
) as res:
    json_data = res.read()

read_json = json.loads(json_data)


def time_stamp(time):
    tz = pytz.timezone(read_json["timezone"])
    return dt.datetime.fromtimestamp(time).now(tz)


timezone = read_json["timezone"]
current_time = time_stamp(read_json["current"]["dt"])
sunrise_time = time_stamp(read_json["current"]["sunrise"])
sunset_time = time_stamp(read_json["current"]["sunset"])

print(f"latitude:{lat},longitude:{lon}, country_code:{c_code}")
print(f"Timezone: {timezone}")
print(f"Current Time: {current_time}")
print(f"Sunrise Time: {sunrise_time}")
print(f"Sunset Time: {sunset_time}")
print(f"Temperature: {read_json['current']['temp']}°C")
print(
    f"Clouds: {read_json['current']['clouds']}%, {read_json['current']['pressure']} hPa"
)
print(f"Humidity: {read_json['current']['humidity']}%")
print(f"Wind: {read_json['current']['wind_speed']} m/s")
print(
    f"Weather: {read_json['current']['weather'][0]['main']}({read_json['current']['weather'][0]['description']})"
)
