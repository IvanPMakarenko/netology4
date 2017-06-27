from urllib.parse import urlencode
import requests

AUTHORIZE_URL = 'https://oauth.yandex.ru/authorize'
APP_ID = '4de696d427cd434e95db4cafda6cd2e0'


auth_data = {
    'response_type': 'token',
    'client_id': APP_ID
}

print('?'.join((AUTHORIZE_URL, urlencode(auth_data))))

TOKEN = 'AQAAAAAVU_MXAARiuEkjNbhOb0xxqhBiyRhMPMw'

class YandexMetrika:
    token = None
    API_MANAGEMENT_URL = 'https://api-metrika.yandex.ru/management/v1/counters ?'
    API_STAT_URL = 'https://api-metrika.yandex.ru/stat/v1/data ?'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Authorization': 'OAuth {0}'.format(self.token),
            'Content - Type': 'application/json'
        }

    def get_counters(self):
        headers = self.get_headers()
        r = requests.get(self.API_MANAGEMENT_URL + 'counters', headers=headers)
        return [
            Counter(self.token, counter['id']) for counter in r.json()['counters']
        ]



class Counter(YandexMetrika):

    def __init__(self, token, counter_id):
        self.counter_id = counter_id
        super().__init__(token)

    def get_metric_data(self, metrics='ym:s:visits'):
        headers = self.get_headers()
        params = {
            'id': self.counter_id,
            'metrics': metrics
        }
        r = requests.get(self.API_STAT_URL + 'data', params, headers=headers)
        #return int(r.json()['data'][0]['metrics'][0]) #если количество просмотров 0, то срипт ломается. Можно конечно
        # try except сделать, но в нашем случае можно использовать инфу из total, т.к. мы каждый раз смотрим 1 метод
        # по 1 счетчику
        return r.json()['totals'][0]


def get_stats():
    metrica = YandexMetrika(TOKEN)
    counters = metrica.get_counters()
    for counter in counters:
        print('Кол-во визитов: {}'.format(counter.get_metric_data('ym:s:visits')))
        print('Кол-во просмотров: {}'.format(counter.get_metric_data('ym:s:pageviews')))
        print('Кол-во посетителей: {}'.format(counter.get_metric_data('ym:s:users')))

get_stats()
