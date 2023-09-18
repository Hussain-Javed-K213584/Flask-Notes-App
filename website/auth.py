from flask import Blueprint, render_template

# This file is a blueprint for our application

auth = Blueprint('auth', __name__)

@auth.route('/login', method=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/logout', method=['GET', 'POST'])
def logout():
    return render_template('login.html')

@auth.route('/sign-up', method=['GET', 'POST'])
def sign_up():
    return render_template('sign_up.html')