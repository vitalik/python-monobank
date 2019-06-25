# python-monobank

Python client for Monobank API (https://api.monobank.ua/docs/)


Usage:

1) Request your token at https://api.monobank.ua/

2) Use that token to initialize client:

```
  token = 'xxxxxxxxxxxxxxx'

  mono = Monobank(token)
  client_info = mono.personal_clientinfo()
  print(client_info)
```


WIP stay tuned
