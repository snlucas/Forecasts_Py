from unittest import TestCase
from controller.forecast_controller import ForecastController
from controller.forecast import Forecast


class TestForecast(TestCase):
    def test_execute_tests(self):
        self.test_forecasts_returns_dict()
        self.test_day_forecast_return_string()
        self.test_week_forecast_return_list()

    def test_forecasts_returns_dict(self):
        fc = ForecastController()
        fc_token = fc.token_as_file('token.txt')
        fc_city = fc.city_forecast('Porto Alegre')

        token = fc.token
        city = fc.city

        f = Forecast(token, city)
        self.assertEqual(type(f.forecasts()), dict, 'Wrong type')

    def test_day_forecast_return_string(self):
        # Test if the value returns a string

        fc = ForecastController()
        fc_token = fc.token_as_file('token.txt')
        fc_city = fc.city_forecast('Porto Alegre')

        token = fc.token
        city = fc.city

        f = Forecast(token, city)
        self.assertIsInstance(f.day_forecast(), str, 'Wrong type')

    def test_week_forecast_return_list(self):
        # Test if the value returns a list

        fc = ForecastController()
        fc_token = fc.token_as_file('token.txt')
        fc_city = fc.city_forecast('Porto Alegre')

        token = fc.token
        city = fc.city

        f = Forecast(token, city)
        self.assertIsInstance(f.week_forecast(), list, 'Wrong type')
