import requests
import json
def  select_currency(message):
    valute = message.text
    valute = str(valute).upper()
    req = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    data = json.loads(req.text)
    valutes = []
    res = {}
    curhelp = []
    for key, value in data.items():
        if type(value) ==  dict:
            for k, v in value.items():
                curhelp.append(k+": "+str(v["Nominal"])+" "+v["Name"])
                valutes.append(k)
                if k == valute:
                    res = v
    if valute == "CURHELP":
        return '\n'.join(curhelp)
    if res == {}:
        return 'Такой валюты нет.\nСписок можно посмотреть по команде "Curhelp"'
    return f'{res["Nominal"]} {res["Name"]} стоит {res["Value"]} рублей'