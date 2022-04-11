import unittest
from mongoengine import connect, disconnect
from api.db.db import Item, Character, Quest, Event, Location


class TestItem(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls) -> None:
        disconnect()

    def test_thing(self):
        item = Item(name='test_item', weight=4.20, description='this is a test item')
        item.save()

        fresh_item = Item.objects().first()
        assert fresh_item.name == 'test_item'
        assert fresh_item.weight == 4.20
        assert fresh_item.description == 'this is a test item'


class TestCharacter(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls) -> None:
        disconnect()

    def test_thing(self):
        item = Item(name='test_item', weight=4.20, description='this is a test item')
        item.save()

        fresh_item = Item.objects().first()
        assert fresh_item.name == 'test_item'
        assert fresh_item.weight == 4.20
        assert fresh_item.description == 'this is a test item'


class TestEvent(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls) -> None:
        disconnect()

    def test_thing(self):
        item = Item(name='test_item', weight=4.20, description='this is a test item')
        item.save()

        fresh_item = Item.objects().first()
        assert fresh_item.name == 'test_item'
        assert fresh_item.weight == 4.20
        assert fresh_item.description == 'this is a test item'


class TestQuest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls) -> None:
        disconnect()

    def test_thing(self):
        item = Item(name='test_item', weight=4.20, description='this is a test item')
        item.save()

        fresh_item = Item.objects().first()
        assert fresh_item.name == 'test_item'
        assert fresh_item.weight == 4.20
        assert fresh_item.description == 'this is a test item'


class TestLocation(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        connect('mongoenginetest', host='mongomock://localhost')

    @classmethod
    def tearDownClass(cls) -> None:
        disconnect()

    def test_thing(self):
        item = Item(name='test_location', description='this is a test location')
        item.save()

        fresh_item = Item.objects().first()
        assert fresh_item.name == 'test_location'
        assert fresh_item.description == 'this is a test location'

