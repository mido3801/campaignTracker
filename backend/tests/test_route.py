import unittest.mock

import pytest
from flask import Flask
from api.app.app import register_route
from api.routes.route import Route
import mongoengine as me
from mongomock import MongoClient


class MockObject(me.Document):
    field = me.StringField()


@pytest.fixture()
def app():
    app = Flask(__name__)
    app.config.update({
        "TESTING": True
    })
    app.db = MongoClient()
    me.connect('mongoenginetest', host='mongomock://localhost')
    register_route(app,
                   Route(MockObject),
                   MockObject,
                   'mock_api',
                   '/backend/mock/')
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_empty_items(client):
    response = client.get('/backend/mock/', json={})
    assert response.data == b'[]'


def test_get_item(client):
    pass
