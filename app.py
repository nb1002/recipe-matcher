import flask
from flask.templating import render_template
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
        new_user = User(name=input['name'], email=input['email'], password= hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        print("pushed")
        return flask.redirect('/login') 

    @app.route("/login")
    def login():
        return flask.render_template('login.html')


    @app.route('/login', methods= ['POST'])
    def plogin():
        input = flask.request.form

        # get email from input
        email_input = input['email']
        pw_input = hashlib.sha256(input['password'].encode('utf-8')).hexdigest()

        # look for match in db
        result = db.session.query(User).filter_by(email= email_input , password = pw_input).first() 

        if result is None:
            return "invalid login info"
            
        else: 
            # make jwt and set cookies
            token = flask_jwt_extended.create_access_token(identity = email_input)
            response = flask.Response("login successful")
            flask_jwt_extended.set_access_cookies(response, token)

            #if successful redirect to front
            return flask.redirect('/front')
            
    @app.route('/front')
    def frontpage(): 
        recipe =  db.session.query(Recipe).filter_by(recipeid = 1).first_or_404()
    
        return flask.render_template('front.html', recipe=recipe)

    @app.route("/test") #initialized flask app
    def helloworld(): #added helloworld endpoint
        return "helloworld"

    return app

#name
if __name__ == "__main__":
    create_app().run(debug=True)

