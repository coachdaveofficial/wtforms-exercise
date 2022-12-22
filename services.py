from models import Pet, db, connect_db


def get_all_pets():
    return Pet.query.all()
def get_pet_by_id(id):
    return Pet.query.get_or_404(id)

