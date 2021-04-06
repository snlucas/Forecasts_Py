from datetime import datetime
import requests
import json


city = input('City Name: ')
lat = ''
lon = ''
units = 'metric'  # Measure units
token = ''
days_forecast = []

# Secret Key
with open('token.txt', 'r') as file:
    token = file.read()

url_city = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'

request_city = requests.get(url_city).json()  # Get data from the API in JSON format

lat = request_city["coord"]["lat"]
lon = request_city["coord"]["lon"]

url_forecasts = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly&appid={token}&units={units}'

request_one_call = requests.get(url_forecasts).json()
daily = request_one_call["daily"]

# Make a list converting unix date format for human readable date format considering month/day
days = [datetime.utcfromtimestamp(int(day["dt"])).strftime('%m/%d') for day in daily]
forecasts = [day["weather"][0]["description"] for day in daily]
days_forecasts = dict.fromkeys(days, '')

for day in range(len(days)):
    days_forecasts[days[day]] = forecasts[day]

for day in days_forecasts:
    print(f'{day} - {days_forecasts[day]}')
