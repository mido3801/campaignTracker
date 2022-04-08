from random import randint
import mongoengine as me
from flask_mongoengine import MongoEngine
from werkzeug.security import generate_password_hash, check_password_hash

db = MongoEngine()


class Item(db.EmbeddedDocument):
    """
    Model for items
    """
    name = me.StringField(required=True)
    weight = me.FloatField()
    description = me.StringField()


class Location(db.EmbeddedDocument):
    """
    Model for locations of interest
    """
    name = me.StringField()
    description = me.StringField()


class Character(db.EmbeddedDocument):
    """
    Model for characters
    """
    name = me.StringField(required=True)
    strength = me.IntField(required=True, default=lambda x: stat_roll())
    constitution = me.IntField(required=True, default=lambda x: stat_roll())
    wisdom = me.IntField(required=True, default=lambda x: stat_roll())
    dexterity = me.IntField(required=True, default=lambda x: stat_roll())
    intelligence = me.IntField(required=True, default=lambda x: stat_roll())
    charisma = me.IntField(required=True, default=lambda x: stat_roll())
    hp = me.IntField(required=True, default=lambda x: stat_roll())
    inventory = me.EmbeddedDocumentListField(Item)


class Event(db.EmbeddedDocument):
    """
    Model for narrative event
    """
    event_characters = me.EmbeddedDocumentListField(Character)
    event_location = me.EmbeddedDocumentField(Location)
    event_items = me.EmbeddedDocumentListField(Item)


class Quest(db.EmbeddedDocument):
    """
    Model for quests
    """
    giver = me.EmbeddedDocumentField(Character)
    goal = me.StringField()
    failure_conditions = db.StringField()


class User(db.Document):
    username = me.StringField()
    password = me.StringField()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def check_jwt_auth_active(self):
        return self.jwt_auth_active

    def set_jwt_auth_active(self, set_status):
        self.jwt_auth_active = set_status

def stat_roll():
    """
    Roll for character stat
    4d6, take highest 3
    :return int: sum of highest 3 rolls
    """
    rolls = [randint(1,7) for x in range(4)]
    rolls.sort()
    return sum(rolls[1:])