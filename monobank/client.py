import requests
from monobank.utils import to_timestamp

ENDPOINT = 'https://api.monobank.ua'


class MonobankError(Exception):
    pass


class MonobankTooManyRequests(Exception):
    pass


class Monobank(object):
    def __init__(self, token):
        self.token = token

    def _get_headers(self):
        return {
            'X-Token': self.token,
            'User-Agent': 'python-monobank (https://github.com/vitalik/python-monobank, contact: ppr.vitaly@gmail.com)'
        }

    def make_request(self, path):
        headers = self._get_headers()
        response = requests.get(ENDPOINT + path, headers=headers)
        if response.status_code == 200:
            return response.json()
        
        if response.status_code == 429:
            raise MonobankTooManyRequests("Too many requests")
        
        data = response.json()
        message = data.get('errorDescription', str(data))
        raise MonobankError(f'{response.status_code} {message}')

    def bank_currency(self):
        return self.make_request('/bank/currency')

    def personal_clientinfo(self):
        return self.make_request('/personal/client-info')
    
    def personal_statement(self, account, date_from, date_to):
        assert date_from <= date_to
        t_from, t_to = to_timestamp(date_from), to_timestamp(date_to)
        url = '/personal/statement/%s/%s/%s' % (account, t_from, t_to)
        return self.make_request(url)
