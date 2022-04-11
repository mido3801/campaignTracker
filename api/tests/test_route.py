import pytest
from flask import Flask


@pytest.fixture()
def app():
    app = Flask()
    app.config.update({
        "TESTING": True
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()



