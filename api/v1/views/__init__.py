from flask import Blueprint

# Create a Blueprint named 'app_views' with the URL prefix '/api/v1'
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import the routes from index.py, states.py, cities.py, amenities.py, users.py, places.py, and places_reviews.py
from api.v1.views import index
from api.v1.views import states
from api.v1.views import cities
from api.v1.views import amenities
from api.v1.views import users
from api.v1.views import places
from api.v1.views import places_reviews

