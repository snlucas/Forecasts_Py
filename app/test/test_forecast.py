from unittest import TestCase
from controller.forecast_controller import ForecastController
from controller.forecast import Forecast


class TestForecast(TestCase):
    def test_execute_tests(self):
        self.test_forecasts_returns_dict()
        self.test_day_forecast_set_string()
        self.test_week_forecast_set_list()

    def test_forecasts_returns_dict(self):
        fc = ForecastController()
        fc_token = fc.token_as_file('token.txt')
        fc_city = fc.city_forecast('Porto Alegre')

        token = fc.token
        city = fc.city

        f = Forecast(token, city)
        self.assertEqual(type(f.forecasts()), dict, 'Wrong type')

    def test_day_forecast_set_string(self):
        # Test if the value changes,
        # and if the value is a string

        fc = ForecastController()
        fc_token = fc.token_as_file('token.txt')
        fc_city = fc.city_forecast('Porto Alegre')

        token = fc.token
        city = fc.city

        f = Forecast(token, city)
        day_forecast_init = f._day_forecast
        fd = f.day_forecast()
        day_forecast_later = f._day_forecast
        self.assertNotEqual(day_forecast_init, day_forecast_later, 'Value hasnt changed')
        self.assertIsInstance(day_forecast_later, str, 'Wrong type')

    def test_week_forecast_set_list(self):
        # Test if the value changes,
        # and if the value is a list

        fc = ForecastController()
        fc_token = fc.token_as_file('token.txt')
        fc_city = fc.city_forecast('Porto Alegre')

        token = fc.token
        city = fc.city

        f = Forecast(token, city)
        week_forecast_init = f._week_forecast
        fw = f.week_forecast()
        week_forecast_later = f._week_forecast
        self.assertNotEqual(week_forecast_init, week_forecast_later, 'Value hasnt changed')
        self.assertIsInstance(week_forecast_later, list, 'Wrong type')
