from django.shortcuts import render
from django.http import HttpResponse
import googlemaps
from datetime import datetime


def index(request, latitude, longitude):
    gmaps = googlemaps.Client(key='AIzaSyBYm9_ggjcyAUFBLBhr8fV79fvNpXUoqOw')
    nearby_restaurants = gmaps.places_nearby(location=(latitude, longitude), radius=10000, language='english',
                                             type='restaurant')
    return HttpResponse(nearby_restaurants['results'])
