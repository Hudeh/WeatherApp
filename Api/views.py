from django.shortcuts import render 
import json 
import urllib.request 
import requests
import datetime
from .api import API_KEY
  

day = datetime.datetime.today() 
weekdays = (day.strftime("%A"))
def index(request): 
    if request.method == 'POST': 
        city = request.POST['city'] 
        source = API_KEY
        # converting JSON data to a dictionary 
        list_of_data = requests.get(source.format(city)).json() 
  
        # data for variable list_of_data 
        data = { 
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
            "name": str(list_of_data['name']), 
            'icon' : list_of_data['weather'][0]['icon'],
            'speed' : str(list_of_data['wind']['speed']),
            'description' : list_of_data['weather'][0]['description'],
        } 
        print(data) 
    else: 
        data ={} 
    context = {
        'data':data,
        'day': day,
        'weekdays':weekdays,
    }
    return render(request, "index.html", context) 
    

def nigeria(request):
    url = API_KEY
    cities =["Abia","Adamawa","Uyo","Anambra","Lagos", "Ogun"]
    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

        weather = {
            "country_code": str(city_weather['sys']['country']), 
            "coordinate": str(city_weather['coord']['lon']) + ' '
                        + str(city_weather['coord']['lat']), 
            "temp": str(city_weather['main']['temp']) + 'k', 
            "pressure": str(city_weather['main']['pressure']), 
            "humidity": str(city_weather['main']['humidity']), 
            "name": str(city_weather['name']), 
            'icon' : city_weather['weather'][0]['icon'],
            'speed' : str(city_weather['wind']['speed']),
            'description' : city_weather['weather'][0]['description'],
        }

        weather_data.append(weather) #add the data for the current city into our list

    context = {'weather_data' : weather_data}
    return render(request, "all-weather.html", context)