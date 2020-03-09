from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_TRACK_MODIFICATIONS =True
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test1.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////D:\\GDrive\\Assignments\\movieRatingSystem\\movieRatingSystem\\test.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test1.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite3')

print(os.path.join(basedir, 'app.sqlite3'))

app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#app.database="sample.db"
db = SQLAlchemy(app)
#db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)