import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent
class DevConfig(object):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR}/data.db"
    SECRET_KEY = os.environ['SECRET_KEY']
