from app import db
class IngInRecipe(db.Model):
    __tablename__ = "IngInRecipe"
    recipeid = db.Column(db.Integer, db.ForeignKey('recipe.recipeid'), primary_key = True, nullable = False)
    ingid = db.Column(db.Integer, db.ForeignKey('ingredients.ingid'), primary_key = True,nullable = False)