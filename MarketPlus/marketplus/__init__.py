# marketplus/__init__.py
from flask import Flask
from flask_caching import Cache
from marketplus.routes import setup_routes  # Ensure you are importing setup_routes

def create_app():
    app = Flask(__name__)

    # Configure Cache (using simple in-memory cache for now)
    app.config['CACHE_TYPE'] = 'SimpleCache'  # You can use 'redis' or other backends for production
    app.config['CACHE_DEFAULT_TIMEOUT'] = 300  # Cache for 5 minutes (300 seconds)

    cache = Cache(app)

    # Pass cache object to routes
    setup_routes(app, cache)

    return app
