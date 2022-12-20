from models import Pet, db, connect_db


def get_all_pets():
    return Pet.query.all()