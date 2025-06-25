from django.shortcuts import render,redirect
from django.contrib import messages
import requests

# Create your views here.

def home(request):
    
    API_KEY = '583f7d1b0ce0d6f2410ca521abb21314'
    contexts={}
    if request.method =='POST':
        city = request.POST.get('city')
        
        geocode_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}'
        geocode_response = requests.get(geocode_url).json()
        
        if not geocode_response:
            messages.error(request,'City not found')
            return render(request,'weather_home.html')
        
        lat = geocode_response[0]['lat']
        lon = geocode_response[0]['lon']
        city = geocode_response[0]['name']
        
        weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
        weather_response = requests.get(weather_url).json()
        
            
        contexts={
            "city":city,
            "climate" : weather_response['weather'][0]['main'],
            "climate_desc" : weather_response['weather'][0]['description'],
            "wind_speed" : weather_response['wind']['speed'],
            "humidity": weather_response['main']['humidity'],
            "temp": weather_response['main']['temp'],
            "icon": weather_response['weather'][0]["icon"]
        }
        
    
    return render(request,'weather_home.html',{"context":contexts})


