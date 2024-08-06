#!/usr/bin/python3
'''Places endpoints'''

from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.place import Place

@app_views.route('/places', strict_slashes=False)
def get_places():
    '''Return a list of all places'''
    places = storage.all(Place).values()
    return jsonify([place.to_dict() for place in places])

