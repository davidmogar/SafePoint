from flask import url_for, render_template, request
from flask.json import dumps
from werkzeug.utils import redirect, escape

from application import app, prefix
from application.model.category import Category
from application.model.report import Report
from application.model.user import User
from application.services import category_service, report_service, user_service

__author__ = 'Dani'


@app.route(prefix + '/init', methods=['GET'])
def init():
    import application.data as data
    from application import db
    from application.persistence import user_persistence, category_persistence, report_persistence

    db.drop_all()
    db.create_all()

    for user_data in data.users:
        user = User(email=user_data['email'],
                    password=user_data['password'],
                    user_id=user_data['id'])
        user_persistence.save(user)

    for category_data in data.categories:
        category = Category(name=category_data['name'],
                            category_id=category_data['id'])
        category_persistence.save(category)

    for report_data in data.reports:
        user_id = report_data['user_id']
        category_id = report_data['category_id']
        report = Report(lat=report_data['lat'],
                        lng=report_data['lng'],
                        description=report_data['description'],
                        time=report_data['time'],
                        user=user_persistence.get(user_id),
                        category=category_persistence.get(category_id),
                        report_id=report_data['id'])
        report_persistence.save(report)
    return redirect(url_for('index'))


@app.route(prefix + '/', methods=['GET'])
def index():
    return render_template('login.html')


@app.route(prefix + '/login', methods=['POST'])
def do_login():
    email = escape(request.form['email'])
    password = request.form['password']
    user = user_service.login(email, password)
    if user is not None:
        return redirect(url_for('static', filename='index.html'))
    return render_template('login.html')


@app.route(prefix + '/categories', methods=['GET'])
def find_categories():
    categories = category_service.get_all()
    return dumps(category_service.categories_to_dict(categories))


@app.route(prefix + '/reports', methods=['GET'])
def find_reports():
    reports = report_service.get_all()
    return dumps(report_service.reports_to_dict(reports))


@app.route(prefix + '/categories/<category_name>/reports', methods=['GET'])
def find_reports_by_category(category_name):
    reports = category_service.get_reports_by_name(category_name)
    return dumps(report_service.reports_to_dict(reports))
