#!/usr/bin/python3
"""
Defining routes for Airbnb clone project
"""
from api.v1.views import app_views
import json
from models import (storage, user, review, city, amenity, place, state)


@app_views.route('/status')
def get_status():
    """returns status code for route /status"""
    return json.dumps({"status": "OK"})


@app_views.route('/stats')
def get_stats():
    """retrieves the number of each objects by type"""
    amenities = storage.count(amenity.Amenity)
    users = storage.count(user.User)
    reviews = storage.count(review.Review)
    cities = storage.count(city.City)
    places = storage.count(place.Place)
    states = storage.count(amenity.Amenity)
    objects = {"amenities": amenities,
               "cities": cities, "places": places,
               "reviews": reviews, "states": states, "users": users}
    return json.dumps(objects)
