import requests
import monobank

ENDPOINT = 'https://api.monobank.ua'
UAGENT = 'python-monobank (https://github.com/vitalik/python-monobank, contact: ppr.vitaly@gmail.com)'


def api_request(method, path, **kwargs):
    "Handles all HTTP requests for monobank endponts"
    headers = kwargs.pop('headers')
    headers['User-Agent'] = UAGENT
    url = ENDPOINT + path
    # print(method, url, headers)
    response = requests.request(method, url, headers=headers, **kwargs)
    
    if response.status_code == 200:
        if not response.content:  # can be just empty an response, but it's fine
            return None
        return response.json()
    
    if response.status_code == 429:
        raise monobank.TooManyRequests("Too many requests", response)
    
    data = response.json()
    message = data.get('errorDescription', str(data))
    raise monobank.Error(message, response)
