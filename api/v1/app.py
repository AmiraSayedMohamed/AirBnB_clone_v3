#!/usr/bin/python3
"""Flask server (variable app)"""

from flask import Flask, jsonify
from os import getenv
from models import storage
from api.v1.views import app_views
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Initialize CORS

app.register_blueprint(app_views)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def teardown(self):
    """Close the storage on teardown"""
    storage.close()

@app.errorhandler(404)
def page_not_found(error):
    """Return a JSON response for 404 errors"""
    return jsonify(error='Not found'), 404

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)

