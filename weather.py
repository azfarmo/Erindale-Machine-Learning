# Python program to find current 
# weather details of any city 
# using openweathermap api 

# import required modules 
import requests, json 
import sys
# Enter your API key here 


# get method of requests module 
# return response object 

# json method of response object 
# convert json format data into 
# python format data 

# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
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
