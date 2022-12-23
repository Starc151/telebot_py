import requests
import json

req = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
data = json.loads(req.text)

date = ""
valutes = []
change = "JPY"
res = {}
for key, value in data.items():
    if key == "Date":
        date = value
    if type(value) ==  dict:
        for k, v in value.items():
            valutes.append(k)
            if k == "JPY":
                res = v
print(res["Name"])
