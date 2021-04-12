from unittest import main
from test import test_forecast_controller, test_forecast


#tfc = test_forecast_controller.TestForecastController().test_execute_tests()
tf = test_forecast.TestForecast().test_execute_tests()

if __name__ == '__main__':
    main()
