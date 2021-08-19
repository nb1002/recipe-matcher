from app import db

class Recipe(db.Model):
    __tablename__ = "recipe"

    recipeid = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String, nullable = False)
    serving = db.Column(db.Integer)
    cooktime = db.Column(db.String)
    img = db.Column(db.String)
    directions = db.Column(db.String)
    favorites = db.relationship('userFavorites')
    ingrecipe = db.relationship('IngInRecipe')