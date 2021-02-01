from django.shortcuts import render, redirect
import requests
from django.contrib import messages
from .models import City
from .forms import CityForm
from .funck import list_sities

def temp(request):
    api_key= '0d57f4e6312f84ad6b4a13c730eb6563'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+api_key
    cities = City.objects.all()
    all_cities = []
    city_name = []
    for city in cities:
        city_name.append(city.name)

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.data['name'] in list_sities():
            if form.data['name'] in city_name:
                messages.error(request, 'city already added')
                #redirect('weather')
            else:
                form.save()
                messages.success(request, 'City add')
                #redirect('weather')
        else:
            messages.error(request, f'Belarusian cities are : {list_sities()}')
    form = CityForm()
    for city in cities:
        resp = requests.get(url.format(city.name)).json()
        city_info = {
            'city_id': city.pk,
            'city': city.name,
            'temp': resp['main']['temp'],
            'icon': resp['weather'][0]['icon'],
            'f_like': resp['main']['feels_like']
        }
        all_cities.append(city_info)
    con = {
        'all_info': all_cities,
        'form' : form
    }
    return render(request,'weather.html',con)

def city_del(request,pk):
    citi = City.objects.get(pk=pk)
    citi.delete()
    return redirect('weather')
