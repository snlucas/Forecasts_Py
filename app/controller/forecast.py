from datetime import datetime
from typing import final
import json
import requests


@final
class Forecast:
    def __init__(self, token, city, units='metric'):
        self._token = token
        self._city = city
        self._units = units
        self._lat = ''
        self._lon = ''
        self.get_coordinates(self._city, self._token)

    def get_coordinates(self, city, token):
        # Needed to get longitude and latitude
        url_city = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'

        request_city = requests.get(url_city).json()  # Get data from the API as JSON
        
        self._lat = request_city["coord"]["lat"]
        self._lon = request_city["coord"]["lon"]

    def forecasts(self):
        '''
        Get a dict of the present week forecasts.
        Keys: days of the week
        Values: forecasts of the week

        token: Your OpenWeather API Key
        '''

        url_forecasts = f'https://api.openweathermap.org/data/2.5/onecall?lat={self._lat}&lon={self._lon}&exclude=minutely,hourly&appid={self._token}&units={self._units}'

        request_one_call = requests.get(url_forecasts).json()
        daily = request_one_call["daily"]

        # Make a list converting unix date format for human readable date format considering month/day
        days = [datetime.utcfromtimestamp(int(day["dt"])).strftime('%m/%d') for day in daily]
        forecasts = [day["weather"][0]["description"] for day in daily]
        week_forecast = dict.fromkeys(days, '')

        for day in range(len(days)):
            week_forecast[days[day]] = forecasts[day]

        return week_forecast

    def day_forecast(self):
        # Set the current day and forecast
        day = next(iter(self.forecasts()))
        forecast = list(self.forecasts().values())[0]

        return f'{day} - {forecast}'

    def week_forecast(self):
        week_forecast = []

        for day in self.forecasts():
            week_forecast.append(f'{day} - {self.forecasts()[day]}')

        return week_forecast

    def __str__(self):
        return self.day_forecast
