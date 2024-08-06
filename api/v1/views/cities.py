#!/usr/bin/python3
'''Cities endpoints'''

from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.city import City

@app_views.route('/cities', strict_slashes=False)
def get_cities():
    '''Return a list of all cities'''
    cities = storage.all(City).values()
    return jsonify([city.to_dict() for city in cities])

