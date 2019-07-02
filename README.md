# python-monobank

![python-monobank](https://raw.githubusercontent.com/vitalik/python-monobank/master/docs/logo.png)

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
  import monobank
  token = 'xxxxxxxxxxxxxxx'

  mono = monobank.Client(token)
  user_info = mono.personal_clientinfo()
  print(user_info)
```

### Methods

Get currencies

```
>>> mono.bank_currency()
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
>>> mono.personal_clientinfo()
{
  'name': 'Dmitriy Dubilet'
  'accounts': [
    {
      'id': 'accidxxxxx'
      'balance': 100000000,
      'cashbackType': 'UAH',
      'creditLimit': 100000000,
      'currencyCode': 980,
      }
  ],
}

```


Get statements
```
>>> mono.personal_statement('accidxxxxx', date(2019,1,1), date(2019,1,30))
[
  {
    'id': 'iZDPhf8v32Qass',
    'amount': -127603,
    'balance': 99872397,
    'cashbackAmount': 2552,
    'commissionRate': 0,
    'currencyCode': 978,
    'description': 'Smartass club',
    'hold': True,
    'mcc': 5411,
    'operationAmount': 4289,
    'time': 1561658263
  },
  ...
]
```




## Corporatre API

...still negotiating...

## Handling Errors

TODO
