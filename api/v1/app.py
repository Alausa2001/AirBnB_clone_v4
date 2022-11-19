#!/usr/bin/python3
"""Inintialize APIs"""
from os import getenv
from Flask import Flask, Blueprint, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS


app = Flask(__name__)


app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_down(error):
    """Removes the SQLAlchemy session"""
    storage.close()


@pp.errorhandler(404)
def not_found(message):
    """Handler for 404 errors.
           Parameters:
               message [str]: message to display.
           Returns:
               The HTTP response.
    """
    response = jsonify({"error": "Not found"})
    response.satus_code = 404
    return response


if __name__ == "__main__":
    app.run(
        host=getenv('HBNB_API_HOST', default='0.0.0.0'),
        port=int(getenv('HBNB_API_PORT', default=5000)),
        threaded=True
    )
