from flask import Flask
from flask import Flask, render_template, redirect, url_for, request, escape, flash, session
app = Flask(__name__)

app.secret_key = "adsadasd"


@app.route('/')
def index():
    return '<h1>Hello there u!</h1>'


# calluing url http://127.0.0.1:5000/welcome?name=noname
@app.route('/welcome')
def welcome():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/template')
def template():
    return render_template('welcome.html')  # sample template rendering


@app.route('/home')
def home():
    return render_template('home.html')  # sample template rendering


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    flash('hello test123')
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
            #return "hi"
        else:
            session['logged_in'] = True
            #return redirect(url_for('/home'))
            return redirect(url_for('home'))
            #return "hi"
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('welcome'))
