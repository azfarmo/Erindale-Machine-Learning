from flask import Flask,render_template, jsonify, request
from weather import get_weather_data
from model import predict
import plotly.express as px
import json
import plotly
import pandas as pd
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
    data = pd.DataFrame({'average_humidity':[17.58,humidity],'type':['average','actual'],'average_temp':[19.76,temp],'noise':[670.6984,int(open('noise.txt','r').read())]})
    graph_humidity = px.bar(data,x="type",y="average_humidity")
    graph_temp = px.bar(data,x='type',y='average_temp')
    graph_noise = px.bar(data,x='type',y='noise')
    graph_humidity = json.dumps(graph_humidity, cls=plotly.utils.PlotlyJSONEncoder)
    graph_temp = json.dumps(graph_temp, cls=plotly.utils.PlotlyJSONEncoder)
    graph_noise = json.dumps(graph_noise, cls=plotly.utils.PlotlyJSONEncoder)
    temp = (temp-273.15) * 9/5 + 32
    return render_template('index.html',graph_temp=graph_temp,graph_noise=graph_noise,graph_humidity=graph_humidity,x = int(predict(temp,humidity,lat,lng)),noise=int(open('noise.txt','r').read()),tem = round(temp,2), hum = round(humidity,2),lat =lat,long = lng)


@app.route('/works')
def how_it_works():
    return render_template('c')
@app.route('/maps')
def maps():
    return render_template('maps.html')
@app.route('/signal')
def signal():
    return render_template('signal.html')
if __name__ == "__main__":
    app.run(debug=True,port=3007)