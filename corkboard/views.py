from django.shortcuts import render
from django.http import HttpResponse
import googlemaps
from datetime import datetime
from corkboard.models import User


def index(request, latitude, longitude, username):
    gmaps = googlemaps.Client(key='AIzaSyBYm9_ggjcyAUFBLBhr8fV79fvNpXUoqOw')
    nearby_restaurants = gmaps.places_nearby(location=(latitude, longitude), radius=10000, language='english',
                                             type='restaurant')
    user = User.objects.get(username=username)
    #sorted_restaurants = sorted(nearby_restaurants['results'], key=lambda x : rate_restaurant(gmaps,x,user), reverse=True)
    
    return HttpResponse(nearby_restaurants['results'])

def rate_restaurant(gmaps, restaurant, user):
    '''
    api call to gmaps.place(restaurant_id)
    chrome: http://127.0.0.1:8000/corkboard/restaurants/latitude/<latitude>/longitude/<longitude>/username/<username>
    1) get executive summary
    2) if food or cuisine is in the executive summary take the user rating into account

    Code:
    1) get executive summary using api call to gmaps.place(restaurant_id)
    2) iterate over dish ratings
    3) check if cuisine or food is in the executive summary
    4) if cuisine or food is in the executive summary 
        a) combine the restuarant rating and the user rating for the dish
    5) return restaurant rating
    '''
    print(restaurant['place_id'])
    pass
"""
users = User.objects.
all = gets all users information
get = get a single users information
filter = get all users that match the paramaters

Use the information that you get from a single user to come up with a rating for local restaurants
Ratings are based off the user query and the rating of the restaurants nearby
Ratings Based Off
"""