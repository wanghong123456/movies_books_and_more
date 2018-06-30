from flask import Flask, render_template

from App.settings import config
from App.extensions import config_extensions
# from App.views import config_blueprint


def createApp(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # Initialize app functions to all third-party extension libraries
    config_extensions(app)
    # Register all of the blueprint functions
    # config_blueprint(app)
    errors(app)
    return app


# Customize a function to capture the error
def errors(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/error404.html')

    def server_error(e):
        return render_template('errors/error500.html')
