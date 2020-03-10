from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_TRACK_MODIFICATIONS =True
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite3')

print(os.path.join(basedir, 'app.sqlite3'))

app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)



class User1(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')



