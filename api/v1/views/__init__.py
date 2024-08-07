from flask import Blueprint

# Create a Blueprint named 'app_views' with the URL prefix '/api/v1'
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import the routes from various view modules to register them with the Blueprint
from api.v1.views import index
from api.v1.views import states

