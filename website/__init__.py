from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # Initialize the database object
DB_NAME = 'database.db' # Set the name for the database

def create_app():
    app = Flask(__name__) # Init the app
    app.config['SECRET_KEY'] = 'PloSs0xS85BQx6VIHT5FQaVb20V0e6Ky' # Secret key to encrypt sessions and cookies
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # Location for sqlite database
    db.init_app(app)
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/') # Register the blueprint defined in views.py
    app.register_blueprint(auth, url_prefix='/') # Register the blueprint defined in auth.py
    
    return app