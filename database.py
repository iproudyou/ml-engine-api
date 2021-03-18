from .models import db

def get_all(model):
    data = model.query.all()
    return data

def add_instance(model, **kwargs):
    instance = model(**kwargs)
    db.session.add(instance)
    db.session.commit()

def delete_instance(model, id):
    model.query.filter.by(id=id).delete()
    db.session.commit()

def edit_instance(model, id, **kwargs):
    instnace = model.query.filter_by(id=id).all()[0]
    for attr, new_value in kwargs:
        setattr(instance, attr, new_value)
    db.session.commit()