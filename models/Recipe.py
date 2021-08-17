from app import db
class Recipe(db.Model):
    __tablename__ = "recipe"
    recipeid = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String, nullable = False)
    serving = db.Column(db.Integer, nullable = False)
    cooktime = db.Column(db.String, nullable = False)
    img = db.Column(db.String, nullable = False)
    directions = db.Column(db.String, nullable = False)
    favorites = db.relationship('userFavorites')
    ingrecipe = db.relationship('IngInRecipe')