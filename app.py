from flask import Flask,render_template, jsonify, request
from weather import get_weather_data
from model import predict
import json
import requests
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/demo')
def demo():
    url = "https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey=at_t8PI3edTMfOr9Q2JkJbok5B300gr8"
    response = requests.get(url) 
    x = response.json()
    temp, humidity = get_weather_data(x["location"]["lat"],x["location"]["lng"])
    temp = (temp-273.15) * 9/5 + 32
    return render_template('index.html',x = int(predict(temp,humidity,x["location"]["lat"],x["location"]["lng"])),noise=int(open('noise.txt','r').read()),tem = round(temp,2),hum = round(humidity,2),lat = x["location"]["lat"],long = x["location"]["lng"])


@app.route('/works')
def how_it_works():
    return render_template('works.html')
if __name__ == "__main__":
    app.run(debug=True,port=10444)