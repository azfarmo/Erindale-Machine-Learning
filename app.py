from flask import Flask,render_template, jsonify, request
from weather import get_weather_data
from model import predict
import json
import requests
app = Flask(__name__)


@app.route('/')
def home():
    url = "https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey=at_t8PI3edTMfOr9Q2JkJbok5B300gr8"
    response = requests.get(url) 
    x = response.json()
    temp, humidity = get_weather_data('San Jose')
    return render_template('index.html',x = int(predict(temp,humidity,x["location"]["lat"],x["location"]["lng"])))


@app.route('/location')
def index():
    url = "https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey=at_t8PI3edTMfOr9Q2JkJbok5B300gr8"
    response = requests.get(url) 
    x = response.json()

    return str(x["location"]["lat"]) + str(x["location"]["lng"])

if __name__ == "__main__":
    app.run(debug=True,port=10444)