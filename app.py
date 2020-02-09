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
    lat = 43.538797
    lng = -79.666482
    temp, humidity = get_weather_data(lat,lng)
    temp = (temp-273.15) * 9/5 + 32
    return render_template('index.html',x = int(predict(temp,humidity,lat,lng)),noise=int(open('noise.txt','r').read()),tem = round(temp,2),hum = round(humidity,2),lat =lat,long = lng)


@app.route('/works')
def how_it_works():
    return render_template('works.html')
@app.route('/maps')
def maps():
    return render_template('maps.html')
@app.route('/signal')
def signal():
    return render_template('signal.html')
if __name__ == "__main__":
    app.run(debug=True,port=3005)