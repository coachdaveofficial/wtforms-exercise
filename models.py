from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet."""

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    photo_url = db.Column(db.String(), nullable=True, default='https://thecontemporarypet.com/wp-content/themes/contemporarypet/images/default.png')
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String(250), nullable=True, default='No notes yet!')
    available = db.Column(db.Boolean, unique=False, default=True)