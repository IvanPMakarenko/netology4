import requests

API_KEY = 'trnsl.1.1.20170613T151517Z.45c25f3184fa7c8c.7ac1659188824beb11730ae13513b5b648348384'

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

"""
https://translate.yandex.net/api/v1.5/tr.json/translate ? 
key=<API-ключ>
 & text=<переводимый текст>
 & lang=<направление перевода>
 & [format=<формат текста>]
 & [options=<опции перевода>]
 & [callback=<имя callback-функции>]
 """

