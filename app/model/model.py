from sqlalchemy.orm import declarative_base,relationship
from sqlalchemy import Column,String,Integer,ForeignKey
Base = declarative_base()
metadata = Base.metadata

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    email = Column(String, unique=True)
    password =Column(String(), nullable=False,unique=True)
    role_id = Column(Integer(), ForeignKey('role.id'))
    def __init__(self,email ,userpassword,role_id ):
             self.password =userpassword
             self.email=email
             self.role_id=role_id
             

class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer(), primary_key=True)
    role_name=Column(String, unique=True)
    users = relationship('User', backref='role')
    def __init__(self,role_name):
         self.role_name=role_name


 


