# Python program to find current 
# weather details of any city 
# using openweathermap api 

# import required modules 
import requests, json 
import sys
def get_weather_data(city):
    api_key = "d7049abea5754572b7c3894db82e56e7"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city, api_key)
    response = requests.get(url) 
    x = response.json()
    if x["cod"] != "404": 
        y = x["main"]
        current_temperature = y["temp"] 
        current_pressure = y["pressure"] 
        return current_temperature,current_pressure
        
    	# store the value of "main" 
