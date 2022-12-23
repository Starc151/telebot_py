import requests
import json

req = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
json_string = req.text