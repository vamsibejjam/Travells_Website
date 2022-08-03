from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from . models import city,car,place
from datetime import datetime


    
# Create your views here.
def index(request):
    dest=city.objects.all() 
    cars=car.objects.all()
    travell={'dest':dest,'cars':cars}  
    return render(request,'Home.html',travell)

def visit(request,val):

    
    '''y=request.resolver_match.view_name
    x=request.build_absolute_uri().replace('http://127.0.0.1:8000/holiday/','')
    x=x.replace('/','')'''

    city_places=[]
    _city=get_object_or_404(city,city_name=val)
    places=place.objects.filter(city_id=_city.id)
   
   
    
    for city_place in places:
        city_places.append(city_place)

    Data={'places':city_places ,'city':_city}
  
    return render(request,'City_place.html',Data)