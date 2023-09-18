from flask import Blueprint, render_template

# This file is a blueprint for our application

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")