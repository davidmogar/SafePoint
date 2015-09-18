from application.model.user import User
from application.persistence import user_persistence
import hashlib

__author__ = 'Dani'


def get_by_id(user_id):
    return user_persistence.get(user_id)


def get_by_username(username):
    return user_persistence.get_by_username(username)


def signup(username, password):
    user = get_by_username(username)
    if user is not None:
        return None
    password_hash = hashlib.md5(password.encode('utf')).hexdigest()
    user = User(username, password_hash)
    user_persistence.save(user)
    return user


def login(username, password):
    user = get_by_username(username)
    if user is None:
        return None
    password_hash = hashlib.md5(password.encode('utf')).hexdigest()
    if user.password == password_hash:
        return user
    return None
