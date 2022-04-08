from flask_restful import Resource, Api
from flask import Response, request
from db import Character, Location, Item, Event, Quest

api = Api()


def init_route(route):
    """Wrapper to associate our routes with api object as we define them"""
    api.add_resource(route, route.path)


@init_route
class CharactersRoute(Resource):
    path = '/api/characters'

    def get(self) -> Response:
        characters = Character.objects().to_json()
        return Response(characters, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        character = Character(**body).save()
        id = character.id
        return {'id': str(id)}, 200


@init_route
class CharacterRoute(Resource):
    path = '/api/characters/<id>'

    def get(self, id) -> Response:
        character = Character.objects.get(id=id).to_json()
        return Response(character, mimetype="application/json", status=200)

    def put(self, id):
        body = request.get_json()
        Character.objects.get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        Character.objects.get(id=id).delete()
        return '', 200


@init_route
class LocationsRoute(Resource):
    path = '/api/locations'

    def get(self) -> Response:
        locations = Location.objects().to_json()
        return Response(locations, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        location = Location(**body).save()
        id = location.id
        return {'id': str(id)}, 200


@init_route
class LocationRoute(Resource):
    path = '/api/locations/<id>'

    def get(self, id) -> Response:
        location = Location.objects(id=id).to_json()
        return Response(location, mimetype="application/json", status=200)

    def put(self, id):
        body = request.get_json()
        Location.objects.get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        Location.objects.get(id=id).delete()
        return '', 200


@init_route
class ItemsRoute(Resource):
    path = '/api/items'

    def get(self) -> Response:
        items = Item.objects().to_json()
        return Response(items, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        item = Item(**body).save()
        id = item.id
        return {'id': str(id)}, 200


@init_route
class ItemRoute(Resource):
    path = '/api/items/<id>'

    def get(self) -> Response:
        item = Item.objects(id=id).to_json()
        return Response(item, mimetype="application/json", status=200)

    def put(self):
        body = request.get_json()
        Item.objects.get(id=id).update(**body)
        return {'id': str(id)}, 200

    def delete(self):
        Item.objects.get(id=id).delete()
        return '', 200

@init_route
class EventsRoute(Resource):
    path = '/api/events'

    def get(self) -> Response:
        events = Event.objects().to_json()
        return Response(events, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        event = Event(**body).save()
        id = event.id
        return {'id': str(id)}, 200


@init_route
class EventRoute(Resource):
    path = '/api/eventd/<id>'

    def get(self) -> Response:
        event = Event.objects(id=id).to_json()
        return Response(event, mimetype="application/json", status=200)

    def put(self):
        body = request.get_json()
        Event.objects.get(id=id).update(**body)
        return {'id': str(id)}, 200

    def delete(self):
        Event.objects.get(id=id).delete()
        return '', 200


@init_route
class QuestsRoute(Resource):
    path = '/api/quests'

    def get(self) -> Response:
        quests = Quest.objects().to_json()
        return Response(quests, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        quest = Quest(**body).save()
        id = quest.id
        return {'id': str(id)}, 200


@init_route
class QuestRoute(Resource):
    path = '/api/quests/<id>'

    def get(self) -> Response:
        quest = Item.objects(id=id).to_json()
        return Response(quest, mimetype="application/json", status=200)

    def put(self):
        body = request.get_json()
        Quest.objects.get(id=id).update(**body)
        return {'id': str(id)}, 200

    def delete(self):
        Quest.objects.get(id=id).delete()
        return '', 200


@init_route
class TestRoute(Resource):
    path = '/api/test'
    def get(self):
        return {'name': 'mike',
                'about': 'this is a test'}
