from app import db
from app.model import  User

def insert_user(email,password,username):
    msg=''
    check_email=db.session.query(User).filter_by(email=email).first()
    if  check_email is not None  :
         msg="Email is Already Registered"      
    else: 
         new_User=User(email=email,password=password)
         db.session.add(new_User)
         db.session.commit()         
         msg="Registration successfull"
    
    return msg

