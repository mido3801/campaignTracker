from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
import os

from db import db, Character, User, Quest, Event, Item, Location
from config import env_config
from resources import Route

route_configs = [(Route(Character), Character, 'character_api', '/api/characters/'),
                 (Route(Location), Location, 'location_api', '/api/locations/'),
                 (Route(Item), Item, 'item_api', '/api/items/'),
                 (Route(Event), Event, 'event_api', '/api/events/'),
                 (Route(Quest), Quest, 'quest_api', '/api/quests/'),
                 (Route(User), User, 'user_api', '/api/users/')]


def create_app(config_name):
    """
    Application factory pattern
    :return: flask app object
    """
    app = Flask(__name__)
    app.config.from_object(env_config[config_name])

    # Initialize app extensions
    db.init_app(app)
    CORS(app)
    Swagger(app)

    for config in route_configs:
        register_route(app, *config)

    return app


def register_route(app, view, model, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint,model = model)
    app.add_url_rule(url, defaults={pk: None},
                     view_func=view_func, methods=['GET', 'PUT', 'DELETE'])
    app.add_url_rule(url, view_func=view_func, methods=['POST',])
    app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                     methods=['GET'])


if __name__ == '__main__':
    app = create_app(os.getenv("FLASK_ENV"))