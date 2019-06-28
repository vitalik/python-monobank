# python-monobank

Python client for Monobank API (https://api.monobank.ua/docs/)

## Installation

```
pip install monobank
```


# Usage

## Personal api

1) Request your token at https://api.monobank.ua/

2) Use that token to initialize client:

```
  token = 'xxxxxxxxxxxxxxx'

  mono = Monobank(token)
  client_info = mono.personal_clientinfo()
  print(client_info)
```

### Methods

Get currencies

```
[
 {'currencyCodeA': 840,
  'currencyCodeB': 980,
  'date': 1561686005,
  'rateBuy': 25.911,
  'rateSell': 26.2357},
 {'currencyCodeA': 978,
  'currencyCodeB': 980,
  'date': 1561686005,
  'rateBuy': 29.111,
  'rateSell': 29.7513},
  ...
```

Get client info

```
>>> mono
{'accounts': [
    {
      'id': 'EnF45gsdfse-ndf'
      'balance': 100000000,
      'cashbackType': 'UAH',
      'creditLimit': 100000000,
      'currencyCode': 980,
               
      }
  ],
 'name': 'Dmitriy Dubilet'}
```


Get statements
```
TODO
```




## Corporatre API

...still negotiating...
