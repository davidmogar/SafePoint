from application import db

__author__ = 'Dani'


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, username, password, user_id=None):
        self.username = username
        self.password = password
        self.user_id = user_id


