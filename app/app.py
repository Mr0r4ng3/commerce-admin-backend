from flask import Flask
from .config import config
from .database import db, migrate
from models import *
from flask_migrate import Migrate


def create_app(enviroment):

    app = Flask(__name__)
    app.config.from_object(enviroment)

    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db, command='migrate')

    return app


app = create_app(config['development'])


if __name__ == '__main__':
    app.run()
