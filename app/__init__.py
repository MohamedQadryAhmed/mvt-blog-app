from flask import Flask
from flask_migrate import Migrate
from app.config import ProdactionConfig as AppConfig
from app.models import db

def create_app(config_name='dev'):
    app = Flask(__name__)

    #add configuration settings
    current_config = AppConfig[config_name]
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config
    app.config.from_object(current_config)

    #add db configuration
    db.init_app(app)
    migrate = Migrate(app , db , render_as_batch=True)
    