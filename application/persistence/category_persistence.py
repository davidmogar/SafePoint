from application import db
from application.model.category import Category
from sqlalchemy import func

__author__ = 'Dani'


def get(category_id):
    return Category.query.get(category_id)


def get_by_name(name):
    return Category.query.filter(func.lower(Category.name) == func.lower(name)).first()


def get_all():
    return Category.query.all();


def save(category):
    db.session.add(category)
    db.session.commit()
