from flask import Blueprint # blueprint - a collection of routes
from flask import render_template # for rendering the html templates

views = Blueprint("views", "__name__")

@views.route('/')
def home():
    return render_template('login.html')

@views.route('/signup')
def signup():
    return render_template('signup.html')

