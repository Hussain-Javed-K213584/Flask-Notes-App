from . import db # Import the database object we created in __init__.py
from flask_login import UserMixin
from sqlalchemy.sql import func # Import sqlite functions

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

"""
    We define a schema for our users
"""
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')