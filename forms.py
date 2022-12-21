from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, ValidationError
from wtforms.validators import InputRequired, Optional, NumberRange, URL, EqualTo

def pet_check(form, field):
    if field.data.lower() not in ['cat', 'dog', 'porcupine']:
        raise ValidationError('Species must be either cat, dog, or porcupine')

class PetForm(FlaskForm):
    """Form for adding/editing Pet."""

    name = StringField("Name",
                       validators=[InputRequired(message="Pet name cannot be blank."), pet_check])
    species = StringField("Species",
                        validators=[InputRequired(message="Species cannot be blank")])
    photo_url = StringField("Profile Picture",
                        validators=[Optional(), URL()])
    age = IntegerField("Age",
                        validators=[Optional(), NumberRange(max=30)])
    notes = StringField("Notes",
                        validators=[Optional()])
        