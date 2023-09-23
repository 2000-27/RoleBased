from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .config import DevConfig

db = SQLAlchemy()
ma = Marshmallow()

app = Flask(__name__)
from .routes import auth, admin_bp, user_profiles,manager_mp

app.config.from_object(DevConfig)
app.register_blueprint(auth, url_prefix='/api')
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(user_profiles, url_prefix='/user')
app.register_blueprint(manager_mp , url_prefix='/manager')
db.init_app(app)   
