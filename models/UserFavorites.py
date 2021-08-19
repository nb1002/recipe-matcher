from app import db

class userFavorites(db.Model):
    __tablename__ = "user_favorites"

    userid = db.Column(db.Integer, db.ForeignKey('users.userid'), primary_key = True, nullable = False)
    recipeid = db.Column(db.Integer, db.ForeignKey('recipe.recipeid'), primary_key = True, nullable = False)

