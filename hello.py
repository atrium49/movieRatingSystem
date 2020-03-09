from flask import Flask
from flask import Flask, render_template, redirect, url_for, request, escape, flash, session
import sqlite3

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

from flask_wtf import FlaskForm 
from flask_sqlalchemy  import SQLAlchemy

app = Flask(__name__)
#global loginflag
loginflag=False
app.secret_key = "adsadasd"
#app.database="sample.db"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////D:/GDrive/Assignments/movieRatingSystem/movieRatingSystem/sample.db'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////D:\\GDrive\\Assignments\\movieRatingSystem\\movieRatingSystem\\sample.db'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////sample.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////new.db'

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


@app.route('/')
def index():
	#return '<h1>Hello there u!</h1>'
	return render_template('home.html')  # sample template rendering


# calluing url http://127.0.0.1:5000/welcome?name=noname
@app.route('/welcome')
def welcome():
	name = request.args.get("name", "World")
	#return f'Hello, {escape(name)}!'
	return render_template('welcome.html')  # sample template rendering


@app.route('/template')
def template():
	return render_template('welcome.html')  # sample template rendering


# @app.route('/home')
# def home():
# 	return render_template('home.html')  # sample template rendering


@app.route('/signup')
def home():
	return render_template('signup.html')  # sample template rendering


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	c=connect_db()
	#session['logged_in']=False
	
	flash('hello test123')
	#if "session['logged_in']" not in locals():
	#if session['logged_in'] == True:
	global loginflag
	if loginflag==True:
		return redirect(url_for('home'))
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials. Please try again.'
			#return "hi"
		else:
			session['logged_in'] = True
			#return redirect(url_for('/home'))
			loginflag=True
			return redirect(url_for('home'))
			#return "hi"
	c.close()
	return render_template('login.html', error=error)


@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	global loginflag
	loginflag=False
	return redirect(url_for('welcome'))

def connect_db():
	#sqlite3.Connection
	return sqlite3.Connection(app.database)

@app.route('/types')
def types():
	user_ag=request.headers.get('User-Agent')
	return '<p>your agent is {}</p>'.format(user_ag)


if __name__ == '__main__':
    app.run(debug=True)