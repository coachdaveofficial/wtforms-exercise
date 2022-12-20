from flask import Flask, request, redirect, render_template
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from services import get_all_pets
from seed import seed_data

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


app.config['SECRET_KEY'] = "doggies"
debug = DebugToolbarExtension(app)

with app.app_context():
    connect_db(app)

    db.create_all()
    # seed_data()
    


@app.route('/')
def home_page():

    pets = get_all_pets()

    return render_template('homepage.html', pets=pets)
