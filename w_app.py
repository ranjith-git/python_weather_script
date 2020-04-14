from urllib.request import urlopen
import json

YOUR_APP_ID = "90768b2590dceed79369f286990fae0c"
lat = 20.593683
lon = 78.962883
with urlopen(
    f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={YOUR_APP_ID}"
) as res:
    json_data = res.read()

read_json = json.loads(json_data)
dump_json = json.dumps(read_json, indent=2)
print(dump_json)
