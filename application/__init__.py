from flask import Flask
from flask.ext.cors import CORS
from flask.ext.sqlalchemy import SQLAlchemy
import os

__author__ = 'Dani'

prefix = '/safepoint'

app = Flask(__name__, static_path=prefix)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///safepoint.db'
cors = CORS(app, resources=r'*', allow_headers='Content-Type')
db = SQLAlchemy(app)

import application.controller
