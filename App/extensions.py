from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


bootstrap=Bootstrap()
db=SQLAlchemy()
migrate=Migrate()

# Initialize the functions of th whole current application
def config_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    