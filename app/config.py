import os
from dotenv import load_dotenv

load_dotenv()
base_dir = os.path.abspath(os.path.dirname(__file__))
class DevConfig(object):
    TESTING = False
    print("your present directiory is  ss",base_dir)
    SQLALCHEMY_DATABASE_URI = f"sqlite:////{base_dir}/data.db"
    print("your sql uri is ",SQLALCHEMY_DATABASE_URI)
    SECRET_KEY = os.environ['SECRET_KEY']
