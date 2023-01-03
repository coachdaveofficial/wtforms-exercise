from flask import Flask, request, redirect, render_template
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from services import get_all_pets, get_pet_by_id
from seed import seed_data
from forms import PetForm, EditPetForm

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

@app.route("/add/", methods=["GET", "POST"])
def add_pet_form():
    
    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        if len(photo_url) == 0:
            photo_url = None
        
        pet = Pet(name=name, 
                species=species, 
                photo_url=photo_url, 
                age=age, 
                notes=notes)

        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('pet_add_form.html', form=form)

@app.route('/<int:pet_id>/', methods=['GET', 'POST'])
def edit_pet_form(pet_id):
    pet = get_pet_by_id(pet_id)
    form = EditPetForm(obj=pet)
    

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data or None
        pet.available = form.available.data
        pet.notes = form.notes.data

        if len(pet.photo_url) == 0:
            pet.photo_url = None

        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit_pet_form.html', form=form, pet=pet)