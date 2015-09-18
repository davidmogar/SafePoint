from application import db
from application.model.user import User

__author__ = 'Dani'


def get(user_id):
    return User.query.get(user_id)


def get_by_email(email):
    return User.query.filter_by(email=email).first()


def save(user):
    db.session.add(user)
    db.session.commit()
