from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve
# to run the local server, run this python file. to stop the local server use control+C in the terminal
app = Flask(__name__)


@app.route('/')
@app.route('/')
def index():
    # used to just be "Hello World" and a blank white webpage
    return render_template('index.html')


@app.route('/weather')
def get_weather():
    city = request.args.get('city')

# pasted from weather.py
    if not bool(city.strip()):
        city = "Des Moines"

    weather_data = get_current_weather(city)

    # city is not found by API
    if not weather_data['cod'] == 200:
        # "City not found" output this message but instead we render the citynotfound html that we made a copy from index html but with a few edits
        return render_template('city-not-found.html')

    return render_template(
        "weather.html",
        # name is a JSON data object received from the weather API
        title=weather_data["name"],
        status=weather_data["weather"][0]['description'].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}", feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )
# the words to the left are used in the weather.html in line 12-14


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
# 8:07 timeframe. so apparently i was using the global python interpreter, had to switch to the virtual python 3.12.1 interpreter to resolve the from flask error
