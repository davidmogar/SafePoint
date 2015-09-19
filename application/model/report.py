from application import db

__author__ = 'Dani'


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    description = db.Column(db.String)
    time = db.Column(db.BigInteger)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('reports'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('reports'))

    def __init__(self, lat, lng, description, time, user, category, report_id=None):
        self.lat = lat
        self.lng = lng
        self.description = description
        self.time = time
        self.user = user
        self.category = category
        if report_id:
            self.id = report_id
