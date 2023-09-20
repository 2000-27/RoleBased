from sqlalchemy.orm import declarative_base , relationship
from sqlalchemy import Column , String , Integer , ForeignKey
from werkzeug.security import generate_password_hash
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    email = Column(String, unique=True)
    password =Column(String(), nullable=False,unique=True)
    role_id = Column(Integer(), ForeignKey('role.id'))
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
   
class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer(), primary_key=True)
    role_name=Column(String, unique=True)
    users = relationship('User', backref='role')
    


 


