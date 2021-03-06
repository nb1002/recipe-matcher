from enum import unique
from app import db

class User(db.Model):
    __tablename__ = "users"

    userid = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String, nullable = False)
    email = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    favorites = db.relationship('userFavorites')