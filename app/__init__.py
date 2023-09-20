from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from .config import DevConfig


db = SQLAlchemy()
ma = Marshmallow()

app = Flask(__name__)
app.config.from_object(DevConfig)
