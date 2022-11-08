from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(testing=None): # just a parameter to pass in
    # __name__ stores the name of the module we're in
    app = Flask(__name__) # Getting flask more information on where everything lives
    # Tells us what python folder we are currently in 
    # Need this for Flask because Flask finds this useful

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    if testing is None:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI') #'postgresql+psycopg2://postgres:postgres@localhost:5432/breakfasts_development'
    else:
        app.config['TESTING']=True # optional
        app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('TEST_SQLALCHEMY_DATABASE_URI')
    # where database lives

    from app.models.breakfast import Breakfast
    from app.models.menu import Menu
    # imports model breakfast into project so that migrations can pick it up
    # import model Menu so that app can find
    
    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.breakfast import breakfast_bp
    from .routes.menu import menu_bp
    # this blueprint depends on this app and this app depends on this blueprint
    # putting this inside makes it ordered (app creates first, then blueprint)
    app.register_blueprint(breakfast_bp)
    app.register_blueprint(menu_bp)
    
    return app