import flask
import flask_sqlalchemy
import flask_jwt_extended
import dotenv
import os

db = flask_sqlalchemy.SQLAlchemy()
jwt = flask_jwt_extended.JWTManager()
dotenv.load_dotenv()

def create_app():
    app = flask.Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///recipe.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
    app.config['JWT_TOKEN_LOCATION'] = 'cookies'
    db.init_app(app)
    jwt.init_app(app)


    @app.route("/test") #initialized flask app
    def helloworld(): #added helloworld endpoint
        return "helloworld"

    return app



#name
if __name__ == "__main__":
    create_app().run(debug=True)

