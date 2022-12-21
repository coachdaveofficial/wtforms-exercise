from models import Pet, db, connect_db


def get_all_pets():
    return Pet.query.all()
def get_pet_by_id(id):
    return Pet.query.get_or_404(id)

# def add_pet(name,species,photo_url,age,notes):
#     return Pet(name=name, 
#                 species=species, 
#                 photo_url=photo_url, 
#                 age=age, 
#                 notes=notes)