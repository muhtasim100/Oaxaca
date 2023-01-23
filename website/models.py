from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Person(db.Model, UserMixin):
    User_ID = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    permission = db.Column(db.String(100))
