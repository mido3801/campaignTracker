"""Application specific tests"""
import pytest
from api.app.app import create_app


@pytest.fixture()
def app():
    """Create test app instance"""
    test_app = create_app('development')
    test_app.config.update({
        "TESTING": True
    })
    yield test_app
