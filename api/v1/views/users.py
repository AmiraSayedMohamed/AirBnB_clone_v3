#!/usr/bin/python3
'''Users endpoints'''

from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.user import User

@app_views.route('/users', strict_slashes=False)
def get_users():
    '''Return a list of all users'''
    users = storage.all(User).values()
    return jsonify([user.to_dict() for user in users])

