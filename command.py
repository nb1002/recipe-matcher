import flask
command = flask.Blueprint("command", __name__)

@command.cli.command('create_tables')
def create_tables(): 
    from app import db
    db.create_all()
    print("created tables")
