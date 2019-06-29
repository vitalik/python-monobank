import requests
import monobank
from monobank.utils import to_timestamp


ENDPOINT = 'https://api.monobank.ua'
UAGENT = 'python-monobank (https://github.com/vitalik/python-monobank, contact: ppr.vitaly@gmail.com)'


class ClientBase(object):
    
    def _get_headers(self, url):
        raise NotImplementedError('Please implement _get_headers')

    def make_request(self, path):
        url = ENDPOINT + path
        headers = self._get_headers(url)
        headers['User-Agent'] = UAGENT
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        
        if response.status_code == 429:
            raise monobank.TooManyRequests("Too many requests", response)
        
        data = response.json()
        message = data.get('errorDescription', str(data))
        raise monobank.Error(message, response)

    def bank_currency(self):
        return self.make_request('/bank/currency')

    def personal_clientinfo(self):
        return self.make_request('/personal/client-info')
    
    def personal_statement(self, account, date_from, date_to):
        assert date_from <= date_to
        t_from, t_to = to_timestamp(date_from), to_timestamp(date_to)
        url = f'/personal/statement/{account}/{t_from}/{t_to}'
        return self.make_request(url)


class Client(ClientBase):
    "Personal API"

    def __init__(self, token):
        self.token = token

    def _get_headers(self, url):
        return {
            'X-Token': self.token,
        }


class CorporateClient(ClientBase):
    "Corporate API"

    def __init__(self, request_id, app_key, secret_key):
        pass  # WIP
        
    def _get_headers(self, url):
        pass  # WIP
    
    def check(self):
        "Checks if user approved access request"
        try:
            self.make_request('/personal/auth/request')
            return True
        except monobank.Error as e:
            if e.response.status_code == 401:
                return False
            raise
