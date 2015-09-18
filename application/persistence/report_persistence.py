from application import db
from application.model.report import Report

__author__ = 'Dani'


def get(report_id):
    return Report.query.get(report_id)


def get_all():
    return Report.query.all()


def save(report):
    db.session.add(report)
    db.session.commit()
