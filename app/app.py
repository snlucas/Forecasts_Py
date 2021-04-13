from flask import Flask, render_template
from controller.forecast_controller import ForecastController
from controller.forecast import Forecast


app = Flask(__name__)

@app.route("/")
def show_current_forecast():
    fc = ForecastController()
    token_file = 'token.txt'

    if fc.token_as_file(token_file):
        token = fc.token

    city = fc.city_forecast('London')

    forecast = Forecast(token, city)
    
    #return forecast.day_forecast()
    return render_template('current_forecast.html', forecast=forecast.day_forecast(), week_forecast=forecast.week_forecast())

if __name__ == "__main__":
    app.run(debug=True, port=8080)
