from unittest import TestCase
from controller.forecast_controller import ForecastController


class TestForecastController(TestCase):
    def test_execute_tests(self):
        self.test_token_as_string_given_empty_string()
        self.test_token_as_string_given_nonempty_input()
        self.test_token_as_string_given_wrong_type_input()
        self.test_city_forecast_given_wrong_type()
        self.test_token_as_file_given_wrong_file_name()

    def test_token_as_string_given_empty_string(self):
        fc = ForecastController()
        self.assertEqual(fc.token_as_string(''), False, 'String vazia')

    def test_token_as_string_given_nonempty_input(self):
        fc = ForecastController()
        self.assertEqual(fc.token_as_string('41gum_t0k3n'), True, 'String valida')

    def test_token_as_string_given_wrong_type_input(self):
        fc = ForecastController()
        self.assertEqual(fc.token_as_string(4), False, 'Tipo numerico e invalido')
        self.assertEqual(fc.token_as_string([]), False, 'Tipo lista e invalido')
        self.assertEqual(fc.token_as_string({}), False, 'Tipo dict e invalido')
        self.assertEqual(fc.token_as_string(1.1), False, 'Tipo float e invalido')
        self.assertEqual(fc.token_as_string(True), False, 'Tipo bool e invalido')

    def test_city_forecast_given_wrong_type(self):
        fc = ForecastController()
        self.assertEqual(fc.city_forecast(1), False, 'Tipo numerico e invalido')
        self.assertEqual(fc.city_forecast([]), False, 'Tipo lista e invalido')
        self.assertEqual(fc.city_forecast({}), False, 'Tipo dict e invalido')
        self.assertEqual(fc.city_forecast(1.1), False, 'Tipo float e invalido')
        self.assertEqual(fc.city_forecast(True), False, 'Tipo bool e invalido')

    def test_token_as_file_given_wrong_file_name(self):
        fc = ForecastController()
        self.assertEqual(fc.token_as_file('../abc.json'), False)
