from sqlalchemy.orm import declarative_base , relationship
from sqlalchemy import Column , String , Integer , ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    email = Column(String, unique=True)
    password =Column(String(), nullable=False)
    role_id = Column(Integer(), ForeignKey('role.id'),default=3)
    username=Column(String(),nullable=False)
    

class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer(), primary_key=True)
    role_name=Column(String, unique=True)
    users = relationship('User', backref='role')
 