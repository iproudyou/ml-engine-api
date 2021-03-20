from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cats(db.Model):
    __tablename__ = 'cats'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    breed = db.Column(db.String(100)
    )