from forecast import Forecast


class ForecastController:
    def __init__(self):
        self.token = ''
        self.city = ''

    def token_as_string(self, string):
        self.token = string

    def token_as_file(self, file):
        # TODO: File handler
        self.token = ''

    def city_forecast(self):
        city = input('City: ')
        # TODO: Input handler
        self.city = city
