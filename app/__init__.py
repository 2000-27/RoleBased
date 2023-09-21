from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .config import DevConfig


db = SQLAlchemy()
ma = Marshmallow()

app = Flask(__name__)
from .routes import auth

app.config.from_object(DevConfig)
app.register_blueprint(auth, url_prefix='/api')


db.init_app(app)   
