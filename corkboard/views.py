from django.shortcuts import render
from django.http import HttpResponse
import googlemaps
import json
from datetime import datetime
from corkboard.models import User
import requests

'''
User
1) Access data members of user using "user.<data_member>"
'''

def index(request, latitude, longitude, username):
    gmaps = googlemaps.Client(key='AIzaSyBYm9_ggjcyAUFBLBhr8fV79fvNpXUoqOw')
    nearby_restaurants = gmaps.places_nearby(location=(latitude, longitude), radius=10000, language='english',
                                             type='restaurant')
    user = User.objects.get(username=username) # need label for food and cuisine

    def get_restaurant_details(restaurant):
        r = gmaps.place(restaurant['place_id'])['result']
        photo = requests.get(f'https://maps.googleapis.com/maps/api/place/photo?maxwidth=300&photo_reference={r["photos"][0]["photo_reference"]}&key=AIzaSyBYm9_ggjcyAUFBLBhr8fV79fvNpXUoqOw')
        r['picture_url'] = photo.url
        return r
    restaurant_details = map(get_restaurant_details, nearby_restaurants['results'])

    sorted_restaurants = sorted(restaurant_details, key=lambda r : rate_restaurant(gmaps,r,user), reverse=True)
    for r in sorted_restaurants:
        print(r['name'], rate_restaurant(gmaps,r,user))
    return HttpResponse(json.dumps(sorted_restaurants))

def rate_restaurant(gmaps, restaurant, user):
    food_list = [{'rating':user.first_dish, 'foods':['mexican','taco','burrito','asada','pastor']},
                 {'rating':user.second_dish, 'foods':['persian', 'greek', 'mediterranean','pita','koobideh', 'kebabs']},
                 {'rating':user.third_dish, 'foods':['pizza','pepperoni']},
                 {'rating':user.fourth_dish, 'foods':['salad','healthy']},
                 {'rating':user.fifth_dish, 'foods':['sandwich','healthy', 'lettuce']},]
    '''
    api call to gmaps.place(restaurant_id)
    chrome: http://127.0.0.1:8000/corkboard/restaurants/latitude/<latitude>/longitude/<longitude>/username/<username>
    1) get executive summary
    2) if food or cuisine is in the executive summary take the user rating into account
    
    Code: #go through name, editorial_summary overview, reviews
    Rating  = user rating + restaurant rating
    1) get executive summary using api call to gmaps.place(restaurant_id)
    2) iterate over dish ratings
    3) check if cuisine or food is in the executive summary
    4) if cuisine or food is in the executive summary 
        a) combine the restuarant rating and the user rating for the dish
    5) return restaurant rating
    '''
    for food_dict in food_list:
        for food in food_dict['foods']:
            if food in restaurant['name'].lower():
                return food_dict['rating'] + restaurant['rating'] - 3
            if 'editorial_summary' in restaurant:
                if food in restaurant['editorial_summary']['overview'].lower():
                    return food_dict['rating'] + restaurant['rating'] - 3
                for r in restaurant['reviews']:
                    if food in r['text'].lower():
                        return food_dict['rating'] + restaurant['rating'] - 3
    if 'rating' not in restaurant:
        return 0
    return restaurant['rating']
    '''
    print(restaurant['name'])
    print("Rating:", restaurant['rating'])
    print(details['result']['editorial_summary'])
    print(len(details['result']['reviews']))
    [print("REVIEW\n" + x['text']) for x in details['result']['reviews']]
    print()
    '''
"""
users = User.objects.
all = gets all users information
get = get a single users information
filter = get all users that match the paramaters

Use the information that you get from a single user to come up with a rating for local restaurants
Ratings are based off the user query and the rating of the restaurants nearby
Ratings Based Off
"""