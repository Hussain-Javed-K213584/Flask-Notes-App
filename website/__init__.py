from flask import Flask

def create_app():
    app = Flask(__name__) # Init the app
    app.config['SECRET_KEY'] = 'PloSs0xS85BQx6VIHT5FQaVb20V0e6Ky' # Secret key to encrypt sessions and cookies
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app