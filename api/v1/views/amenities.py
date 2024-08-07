#!/usr/bin/python3
'''Amenity endpoints'''

from flask import jsonify, request, abort
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity

@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    '''Retrieve a list of all Amenity objects'''
    amenities = storage.all(Amenity).values()
    return jsonify([amenity.to_dict() for amenity in amenities])

@app_views.route('/amenities/<string:amenity_id>', methods=['GET'], strict_slashes=False)
def get_amenity(amenity_id):
    '''Retrieve a specific Amenity object by ID'''
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())

@app_views.route('/amenities/<string:amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_amenity(amenity_id):
    '''Delete a specific Amenity object by ID'''
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200

@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenity():
    '''Create a new Amenity object'''
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    if 'name' not in data:
        abort(400, description="Missing name")
    new_amenity = Amenity(name=data['name'])
    storage.new(new_amenity)
    storage.save()
    return jsonify(new_amenity.to_dict()), 201

@app_views.route('/amenities/<string:amenity_id>', methods=['PUT'], strict_slashes=False)
def update_amenity(amenity_id):
    '''Update a specific Amenity object by ID'''
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)
    storage.save()
    return jsonify(amenity.to_dict()), 200

