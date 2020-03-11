from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

import os

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite3')

app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True



bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return render_template('signupSuccess.html')
        #return '<h1>New user has been created!</h1>'
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)



class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('home'))

        #return '<h1>Invalid username or password</h1>'
        return render_template('loginFailure.html')
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)


@app.route('/home')
# @login_required
def home():
	#return '<h1>Hello there u!</h1>'
	return render_template('home.html')  # sample template rendering


@app.route('/')
# @login_required
def home2():
	#return '<h1>Hello there u!</h1>'
	return render_template('home.html')  # sample template rendering



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


class NewMovie(FlaskForm):
    MovieTitle = StringField('MovieTitle', validators=[InputRequired(), Length(max=500)])
    MovieDescription = StringField('MovieDescription', validators=[InputRequired(), Length(min=4, max=1500)])
    MovieYear = StringField('MovieYear', validators=[InputRequired(), Length(min=4, max=4)])

class MovieTable( db.Model):
    id = db.Column(db.Integer, primary_key=True)
    MovieTitle = db.Column(db.String(500), unique=True)
    MovieDescription = db.Column(db.String(1500))
    MovieYear = db.Column(db.String(4))

@app.route('/AddMovie', endpoint='AddMovie', methods=['GET', 'POST'])
@login_required
def AddMovie():
    # logout_user()
    #return redirect(url_for('AddMovie.html'))
    form = NewMovie()

    if form.validate_on_submit():
        #hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_movie = MovieTable(MovieTitle=form.MovieTitle.data, MovieDescription=form.MovieDescription.data, MovieYear=form.MovieYear.data,)
        db.session.add(new_movie)
        db.session.commit()
        return render_template('movieAddSuccess.html')    
    return render_template('AddMovie.html', form=form)

#ListMovies


@app.route('/ListMovies', endpoint='ListMovies', methods=['GET', 'POST'])
@login_required
def ListMovies():
    # logout_user()
    #return redirect(url_for('AddMovie.html'))
    movieTable = MovieTable.query.all()

    
    return render_template('ListMovies.html', movieTable=movieTable)


#RemoveMovies

class delMovieForm(FlaskForm):
    options=StringField('options')

@app.route('/RemoveMovies', endpoint='RemoveMovies', methods=['GET', 'POST'])
@login_required
def RemoveMovies():
    # logout_user()
    #return redirect(url_for('AddMovie.html'))
    form = delMovieForm()
    movieTable = MovieTable.query.all()
    print("#########form Started#########")
    if form.validate_on_submit():
        print("#########form validated#########")
        MovieTable.query.filter(MovieTable.id == form.options.data).delete()
        db.session.commit()
        return render_template('deleteMovieSuccess.html')    



    
    return render_template('RemoveMovies.html', movieTable=movieTable,form=form)


#ListAllUsers

@app.route('/ListAllUsers', endpoint='ListAllUsers', methods=['GET', 'POST'])
@login_required
def ListAllUsers():
    # logout_user()
    #return redirect(url_for('AddMovie.html'))
    #form = delMovieForm()
    userTable = User.query.all()
    print("#########form Started#########")
    
    
    return render_template('ListAllUsers.html', userTable=userTable)

