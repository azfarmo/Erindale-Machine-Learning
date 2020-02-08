from flask import Flask,render_template
from weather import get_weather_data
from model import predict
app = Flask(__name__)


@app.route('/')
def home():
    temp, humidity = get_weather_data('San Jose')
    return render_template('index.html',x = str(predict(temp,humidity,40.058323,-74.405663)))

if __name__ == "__main__":
    app.run(debug=True,port=10444)