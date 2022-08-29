from flask import Flask

def create_app():
    app = Flask(__name__)

    # importing the blue print and registering it with the app
    from .views import views
    app.register_blueprint(views, url_prefix="/")

    # my name is abiraam

    return app

