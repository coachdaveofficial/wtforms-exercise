from flask import Flask, request, redirect, render_template
from models import db, connect_db
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


app.config['SECRET_KEY'] = "doggies"
debug = DebugToolbarExtension(app)

with app.app_context():
    connect_db(app)

    db.create_all()


@app.route('/')
def home_page():
    