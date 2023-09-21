from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .config import DevConfig


db = SQLAlchemy()
ma = Marshmallow()

app = Flask(__name__)
from .routes import sign , Login

app.config.from_object(DevConfig)
app.register_blueprint(Login, url_prefix='/api')
app.register_blueprint(sign, url_prefix='/api')

db.init_app(app)   
