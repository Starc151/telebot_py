import requests
import json
def  select_currency(message):
    valute = message.text
    valute = str(valute).upper()
    req = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    data = json.loads(req.text)
    valutes = []
    res = {}
    # curhelp = []
    for key, value in data.items():
        if type(value) ==  dict:
            for k, v in value.items():
                # curhelp.append(k+": "+str(v["Nominal"])+" "+v["Name"])
                valutes.append(k)
                if k == valute:
                    res = v
    # if valute == "CURHELP":
    #     return '\n'.join(curhelp)
    if res == {}:
        return 'Такой валюты нет.\nСписок можно посмотреть по команде "Curhelp"'
    return f'{res["Nominal"]} {res["Name"]} стоит {res["Value"]} рублей'

def dict_valutes():
    dict_valutes = {'AUD': '1 Австралийский доллар',
                    'AZN': '1 Азербайджанский манат',
                    'GBP': '1 Фунт стерлингов Соединенного королевства',
                    'AMD': '100 Армянских драмов',
                    'BYN': '1 Белорусский рубль',
                    'BGN': '1 Болгарский лев',
                    'BRL': '1 Бразильский реал',
                    'HUF': '100 Венгерских форинтов',
                    'HKD': '10 Гонконгских долларов',
                    'DKK': '10 Датских крон',
                    'USD': '1 Доллар США',
                    'EUR': '1 Евро',
                    'INR': '100 Индийских рупий',
                    'KZT': '100 Казахстанских тенге',
                    'CAD': '1 Канадский доллар',
                    'KGS': '100 Киргизских сомов',
                    'CNY': '10 Китайских юаней',
                    'MDL': '10 Молдавских леев',
                    'NOK': '10 Норвежских крон',
                    'PLN': '1 Польский злотый',
                    'RON': '1 Румынский лей',
                    'XDR': '1 СДР (специальные права заимствования)',
                    'SGD': '1 Сингапурский доллар',
                    'TJS': '10 Таджикских сомони',
                    'TRY': '10 Турецких лир',
                    'TMT': '1 Новый туркменский манат',
                    'UZS': '10000 Узбекских сумов',
                    'UAH': '10 Украинских гривен',
                    'CZK': '10 Чешских крон',
                    'SEK': '10 Шведских крон',
                    'CHF': '1 Швейцарский франк',
                    'ZAR': '10 Южноафриканских рэндов',
                    'KRW': '1000 Вон Республики Корея',
                    'JPY': '100 Японских иен'}
    return dict_valutes