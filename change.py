import requests
import json
def  currency_exchange(message):
    valute = message.text
    valute = str(valute).upper()
    req = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    data = json.loads(req.text)
    valutes = []
    res = {}
    for key, value in data.items():
        if type(value) ==  dict:
            for k, v in value.items():
                valutes.append(k)
                if k == valute:
                    res = v
    if res == {}:
        return 'Такой валюты нет.\nСписок кодировок можно посмотреть по кнопке ниже'
    return f'{res["Nominal"]} {res["Name"]} стоит {res["Value"]} рублей'

def valutes():
    valutes = "AUD: 1 Австралийский доллар\n\
AZN: 1 Азербайджанский манат\n\
GBP: 1 Фунт стерлингов Соединенного королевства\n\
AMD: 100 Армянских драмов\n\
BYN: 1 Белорусский рубль\n\
BGN: 1 Болгарский лев\n\
BRL: 1 Бразильский реал\n\
HUF: 100 Венгерских форинтов\n\
HKD: 10 Гонконгских долларов\n\
DKK: 10 Датских крон\n\
USD: 1 Доллар США\n\
EUR: 1 Евро\n\
INR: 100 Индийских рупий\n\
KZT: 100 Казахстанских тенге\n\
CAD: 1 Канадский доллар\n\
KGS: 100 Киргизских сомов\n\
CNY: 10 Китайских юаней\n\
MDL: 10 Молдавских леев\n\
NOK: 10 Норвежских крон\n\
PLN: 1 Польский злотый\n\
RON: 1 Румынский лей\n\
XDR: 1 СДР (специальные права заимствования)\n\
SGD: 1 Сингапурский доллар\n\
TJS: 10 Таджикских сомони\n\
TRY: 10 Турецких лир\n\
TMT: 1 Новый туркменский манат\n\
UZS: 10000 Узбекских сумов\n\
UAH: 10 Украинских гривен\n\
CZK: 10 Чешских крон\n\
SEK: 10 Шведских крон\n\
CHF: 1 Швейцарский франк\n\
ZAR: 10 Южноафриканских рэндов\n\
KRW: 1000 Вон Республики Корея\n\
JPY: 100 Японских иен"
    return valutes