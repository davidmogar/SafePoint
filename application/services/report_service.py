from application.model.report import Report
from application.persistence import report_persistence

__author__ = 'Dani'


def get_by_id(report_id):
    return report_persistence.get(report_id)


def get_all():
    return report_persistence.get_all()


def make_report(lat, lng, description, time, user, category):
    report = Report(lat, lng, description, time, user, category)
    report_persistence.save(report)
    return report


def report_to_dict(report):
    _dict = {
        'id': report.id,
        'lat': report.lat,
        'lng': report.lng,
        'description': report.description,
        'time': report.time,
        'user_id': report.user.user_id,
        'category_id': report.category.category_id
    }
    return _dict


def reports_to_dict(reports):
    return [report_to_dict(report) for report in reports]
