from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from api.config import config_dict
from api.database import db



def create_app(config=config_dict['dev']):
    app= Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate= Migrate(app,db)

    @app.shell_context_processor
    def make_shell_context():
        return {'db': db,
                }

    return app 