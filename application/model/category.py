from application import db

__author__ = 'Dani'


class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, name, category_id=None):
        self.name = name
        if category_id:
            self.category_id = category_id
