#!/usr/bin/python3
'''Amenities endpoints'''

from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity

@app_views.route('/amenities', strict_slashes=False)
def get_amenities():
    '''Return a list of all amenities'''
    amenities = storage.all(Amenity).values()
    return jsonify([amenity.to_dict() for amenity in amenities])

