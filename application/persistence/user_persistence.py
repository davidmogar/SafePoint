from application import db
from application.model.user import User

__author__ = 'Dani'


def get(user_id):
    return User.query.get(user_id)


def get_by_username(username):
    return User.query.filter_by(username=username)


def save(user):
    db.session.add(user)
    db.session.commit()
