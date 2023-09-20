import os
from dotenv import load_dotenv

load_dotenv()
base_dir = os.path.abspath(os.path.dirname(__file__))
class DevConfig(object):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = base_dir+"sqlite:////data.db"
    SECRET_KEY = os.environ['SECRET_KEY']
