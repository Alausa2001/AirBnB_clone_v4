#!/usr/bin/python3
"""Routing for views"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def show_status():
    """Shows the status of the API
         Returns:
             A JSON string of the status
    """
    return jsonify({'status': 'OK'})
