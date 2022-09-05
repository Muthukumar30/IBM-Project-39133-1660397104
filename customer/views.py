from flask import Blueprint
from flask import render_template

views = Blueprint("views", "__name__")

@views.route('/')
def home():
    return render_template('login.html')


@views.route('/settings')
def settings():
    return render_template('settings.html')