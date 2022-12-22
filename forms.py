from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, ValidationError, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL

def pet_check(form, field):
    if field.data.lower() not in ['cat', 'dog', 'porcupine']:
        raise ValidationError(f'Species must be either cat, dog, or porcupine')

class PetForm(FlaskForm):
    """Form for adding Pet."""

    name = StringField("Name",
                       validators=[InputRequired(message="Pet name cannot be blank.")])
    species = StringField("Species",
                        validators=[InputRequired(message="Species cannot be blank"), pet_check])
    photo_url = StringField("Profile Picture URL",
                        validators=[Optional(), URL(message="Please provide valid URL")])
    age = IntegerField("Age",
                        validators=[Optional(), NumberRange(max=30)])
    notes = StringField("Notes",
                        validators=[Optional()])
class EditPetForm(FlaskForm):
    """Form for editing Pet."""

   
    photo_url = StringField("Profile Picture URL",
                        validators=[Optional(), URL(message="Please provide valid URL")])
    notes = StringField("Notes",
                        validators=[Optional()])
    available = BooleanField("Available",
                        validators=[Optional()])
        