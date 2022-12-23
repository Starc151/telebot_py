import requests
import json

req = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
data = json.loads(req.text)

for key, value in data.items():
    if type(value) ==  dict:
        for k, v in value.items():
            print(k)
            for i in v:
                print(v[i])