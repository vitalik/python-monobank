
class Error(Exception):
    def __init__(self, message, response):
        super().__init__(message)
        self.response = response
    
    def __str__(self):
        return f'{self.response.status_code}: {self.args[0]}'


class TooManyRequests(Error):
    pass
