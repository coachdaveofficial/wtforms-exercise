from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Optional, Email

class PetForm(FlaskForm):
    """Form for adding/editing Pet."""

    name = StringField("Name",
                       validators=[InputRequired()])
    species = StringField("Species",
                        validators=[InputRequired()])
    photo_url = StringField("Profile Picture",
                        validators=[Optional()])
    age = IntegerField("Age",
                        validators=[Optional()])
    notes = StringField("Notes",
                        validators=[Optional()])
        