from app import db
from app.model import  User
from flask import request,jsonify
from app.util import email_check,user_check,set_password

def insert_user(email,password,username,role_id):
    msg=''
    check_email=db.session.query(User).filter_by(email=email).first()
    if  check_email is not None  :
         msg="Email is Already Registered"      
    else: 
         new_User=User(email=email,password=password,username=username,role_id=role_id)
         db.session.add(new_User)
         db.session.commit()         
         msg="Registration successfull"
    
    return msg


def insert_into_db():
    msg=''
    json_body = request.get_json()
    username = json_body['username']
    email = json_body['email']
    userpassword = json_body['userpassword']
    confirmpwd = json_body['confirmpwd']
    role_id=json_body['role_id']
    email_ans=email_check(email)
    user_ans=user_check(username)
    if confirmpwd != userpassword: 
             msg="Password and confirm password should be same"
             return msg  
                
    else:
         if email_ans ==True:
               if  user_ans==True :
                    hash_password=set_password(userpassword)    
                    msg=insert_user(email,hash_password,username,role_id)
                    return msg 
               else:
                    msg="Please enter a valid username"
                    return msg  
               
         else :
                msg="Please enter a valid email address"
                return msg  
             
        