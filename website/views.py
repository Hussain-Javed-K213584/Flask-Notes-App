from flask import Blueprint

# This file is a blueprint for our application

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Test</h1>"