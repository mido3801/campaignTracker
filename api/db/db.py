from random import randint
import mongoengine as me
from flask_mongoengine import MongoEngine
from werkzeug.security import generate_password_hash, check_password_hash

db = MongoEngine()


class Item(db.Document):
    """Model for items"""
    name = db.StringField(required=True)
    weight = db.FloatField()
    description = db.StringField()


class Location(db.Document):
    """Model for locations of interest"""
    name = db.StringField()
    description = db.StringField()


class Character(db.Document):
    """Model for characters"""
    name = db.StringField(required=True)
    strength = db.IntField(required=True, default=lambda: stat_roll())
    constitution = db.IntField(required=True, default=lambda: stat_roll())
    wisdom = db.IntField(required=True, default=lambda: stat_roll())
    dexterity = db.IntField(required=True, default=lambda: stat_roll())
    intelligence = db.IntField(required=True, default=lambda: stat_roll())
    charisma = db.IntField(required=True, default=lambda: stat_roll())
    hp = db.IntField(required=True, default=lambda: stat_roll())
    inventory = db.ListField(me.ReferenceField(Item,
                                               reverse_delete_rule=me.PULL))


class Event(db.Document):
    """Model for narrative event"""
    characters = db.ListField(db.ReferenceField(Character,
                                                reverse_delete_rule=me.PULL))
    location = db.ReferenceField(Location, reverse_delete_rule=me.PULL)
    items = db.ReferenceField(Item, reverse_delete_rule=me.PULL)
    description = db.StringField()


class Quest(db.Document):
    """Model for quests"""
    character = db.ReferenceField(Character, reverse_delete_rule=me.PULL)
    goal = db.StringField()
    failure_conditions = db.StringField()


class User(db.Document):
    username = me.StringField()
    password = me.StringField()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


def stat_roll():
    """
    Roll for character stat
    4d6, take highest 3
    :return int: sum of highest 3 rolls
    """
    rolls = [randint(1, 7) for x in range(4)]
    rolls.sort()
    return sum(rolls[1:])
