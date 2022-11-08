import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.breakfast import Breakfast

@pytest.fixture
def app():
    app = create_app({"TESTING": True})
    # create test app instance (flask object)

    @request_finished.connect_via(app) # skip at first, if not finished testing
    def expire_session(sender, response, **extra): # ** any extra variables we may make
        # can declare additional variables
        db.session.remove() # removes db session (if made new instance), to rerun with most updated
        # so all data for each test is up to date

    with app.app_context(): # create all tables within test db
        db.create_all()
        yield app
    
    with app.app_context(): # after finishing request, drop db
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client() # convention with create app, flask client
    # model for running requests and getting responses back

@pytest.fixture
def two_breakfasts(app):
    breakfast1 = Breakfast(name="Cap'n Crunch", rating=3.5, prep_time=3)
    breakfast2 = Breakfast(name="Biscuits n Gravy", rating=5, prep_time=35)

    db.session.add(breakfast1)
    db.session.add(breakfast2)
    db.session.commit()
    