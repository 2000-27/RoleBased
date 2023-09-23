from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .config import DevConfig

db = SQLAlchemy()
ma = Marshmallow()

app = Flask(__name__)
from .routes import auth,Admin,user_profiles

app.config.from_object(DevConfig)
app.register_blueprint(auth, url_prefix='/api')
app.register_blueprint(Admin, url_prefix='/access')
app.register_blueprint(user_profiles, url_prefix='/access')



db.init_app(app)   
