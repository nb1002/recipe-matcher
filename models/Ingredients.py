from app import db

class Ingredients(db.Model):
    __tablename__ = "ingredients"

    ingid = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String, nullable = False)
    ingrecipe =  db.relationship('IngInRecipe')
    counter = db.Column(db.Integer)

    