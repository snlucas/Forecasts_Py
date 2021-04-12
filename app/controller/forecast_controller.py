from controller.forecast import Forecast


class ForecastController:
    def __init__(self):
        self.token = ''
        self.city = ''

    def token_as_string(self, string):
        if isinstance(string, str) and len(string) > 0:
            self.token = string
            return True
        return False

    def token_as_file(self, file):
        try:
            with open(file, 'r') as f:
                token = f.read()
                self.token_as_string(token)
                return True
        except Exception as e:
            print(str(e))
            return False

    def city_forecast(self, city_name):
        if isinstance(city_name, str) and len(city_name) > 0:
            self.city = city_name
            return True
        return False
