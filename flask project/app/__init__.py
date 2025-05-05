from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from dotenv import load_dotenv
import os


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    load_dotenv()
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hemendra:hemendra%4012345@localhost:5432/flask_test'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.users import users_bp
    app.register_blueprint(users_bp)

    with app.app_context():
        db.create_all()
    
    return app