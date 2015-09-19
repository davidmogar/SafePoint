from application import db
from application.model.category import Category

__author__ = 'Dani'


def get(category_id):
    return Category.query.get(category_id)


def get_all():
    return Category.query.all();


def save(category):
    db.session.add(category)
    db.session.commit()
