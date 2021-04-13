from controller.forecast_controller import ForecastController
from controller.forecast import Forecast


fc = ForecastController()
token_file = 'token.txt'

if fc.token_as_file(token_file):
    token = fc.token

city = fc.city_forecast('London')

forecast = Forecast(token, city)
print(forecast.day_forecast())
print('\n==== Week Forecast ====')
for forecast in forecast.week_forecast():
    print(forecast)
