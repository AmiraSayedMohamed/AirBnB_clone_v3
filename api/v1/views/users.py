#!/usr/bin/python3
'''User endpoints'''

from flask import jsonify, request, abort
from api.v1.views import app_views
from models import storage
from models.user import User

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    '''Retrieve a list of all User objects'''
    users = storage.all(User).values()
    return jsonify([user.to_dict() for user in users])

@app_views.route('/users/<string:user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    '''Retrieve a specific User object by ID'''
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())

@app_views.route('/users/<string:user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    '''Delete a specific User object by ID'''
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({}), 200

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    '''Create a new User object'''
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    if 'email' not in data:
        abort(400, description="Missing email")
    if 'password' not in data:
        abort(400, description="Missing password")
    new_user = User(email=data['email'], password=data['password'])
    storage.new(new_user)
    storage.save()
    return jsonify(new_user.to_dict()), 201

@app_views.route('/users/<string:user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    '''Update a specific User object by ID'''
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    for key, value in data.items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, key, value)
    storage.save()
    return jsonify(user.to_dict()), 200

