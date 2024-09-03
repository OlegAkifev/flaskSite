from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from blog.user.views import user
from blog.report.views import report


db = SQLAlchemy()

def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    print("DEBUG:", app.config.get("DEBUG"))
    print("DATABASE_URI:", app.config.get("SQLALCHEMY_DATABASE_URI"))
    print("Secret Key:", app.config.get("SECRET_KEY"))
    db.init_app(app)

    register_blueprints(app)
    return app


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(user)
    app.register_blueprint(report)



