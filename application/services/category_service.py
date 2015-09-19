from application.persistence import category_persistence

__author__ = 'Dani'


def get_by_id(category_id):
    return category_persistence.get(category_id)


def get_all():
    return category_persistence.get_all()


def get_reports_by_id(category_id):
    category = get_by_id(category_id)
    if category:
        return category.reports
    else:
        return []


def category_to_dict(category):
    _dict = {
        'id': category.id,
        'name': category.name
    }
    return _dict


def categories_to_dict(categories):
    return [category_to_dict(category) for category in categories]
