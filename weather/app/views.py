from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def hello(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=3eddb48b4fb12e573021b8e5c4d14aa9'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()

    cities = City.objects.all()
    list_of_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
        }
        list_of_cities.append(city_info)
    context = {'all_info': list_of_cities, 'form': form}

    # print(res.text)
    return render(request, 'app/hello.html', context)