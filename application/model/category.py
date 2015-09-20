from application import db

__author__ = 'Dani'


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    reports = db.relationship('Report', backref='category')

    def __init__(self, name, category_id=None):
        self.name = name
        if category_id:
            self.id = category_id
