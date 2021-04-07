from forecast import Forecast


# Secret Key
token = ''
with open('token.txt', 'r') as file:
    token = file.read()

city = input('city: ')

f = Forecast(token, city)
print(f)
