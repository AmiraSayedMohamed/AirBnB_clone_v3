#!/usr/bin/python3
'''Places endpoints'''

from flask import jsonify, request, abort
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.city import City
from models.user import User

@app_views.route('/cities/<string:city_id>/places', methods=['GET'], strict_slashes=False)
def get_places_by_city(city_id):
    '''Retrieve a list of all Place objects for a specific City'''
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    places = storage.all(Place).values()
    city_places = [place.to_dict() for place in places if place.city_id == city_id]
    return jsonify(city_places)

@app_views.route('/places/<string:place_id>', methods=['GET'], strict_slashes=False)
def get_place(place_id):
    '''Retrieve a specific Place object by ID'''
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())

@app_views.route('/places/<string:place_id>', methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    '''Delete a specific Place object by ID'''
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    storage.delete(place)
    storage.save()
    return jsonify({}), 200

@app_views.route('/cities/<string:city_id>/places', methods=['POST'], strict_slashes=False)
def create_place(city_id):
    '''Create a new Place object'''
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    if 'user_id' not in data:
        abort(400, description="Missing user_id")
    if 'name' not in data:
        abort(400, description="Missing name")
    user = storage.get(User, data['user_id'])
    if user is None:
        abort(404)
    new_place = Place(**data)
    new_place.city_id = city_id
    storage.new(new_place)
    storage.save()
    return jsonify(new_place.to_dict()), 201

@app_views.route('/places/<string:place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    '''Update a specific Place object by ID'''
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    for key, value in data.items():
        if key not in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
            setattr(place, key, value)
    storage.save()
    return jsonify(place.to_dict()), 200

