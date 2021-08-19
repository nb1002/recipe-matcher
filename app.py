import flask
import flask_sqlalchemy
import flask_jwt_extended
import dotenv
import os
import hashlib

db = flask_sqlalchemy.SQLAlchemy()
jwt = flask_jwt_extended.JWTManager()
dotenv.load_dotenv()

def create_app():
    app = flask.Flask(__name__)
    if os.getenv("DATABASE_URL"):
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv["DATABASE_URL"]
    else: 
        app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///recipe.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
    app.config['JWT_TOKEN_LOCATION'] = 'cookies'

    db.init_app(app)
    jwt.init_app(app)

    from models.User import User
    from models.Recipe import Recipe
    from models.Ingredients import Ingredients
    from models.UserFavorites import userFavorites
    from models.IngInRecipe import IngInRecipe
    from command import command
    app.register_blueprint(command)


    @app.route("/signup")
    def signup():
        return flask.render_template('signup.html')

    @app.route("/signup", methods=["POST"])
    def psignup():
        #print(flask.request.form.to_dict())
        #return("success")
        input = flask.request.form
        hashed_pw = hashlib.sha256(input['password'].encode('utf-8')).hexdigest()
        new_user = User(name=input['name'], email=input['email'], password= hashed_pw )
        print(new_user)
        return('success')



    @app.route("/test") #initialized flask app
    def helloworld(): #added helloworld endpoint
        return "helloworld"

    return app


#name
if __name__ == "__main__":
    create_app().run(debug=True)

