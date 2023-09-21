from flask import request , jsonify , Blueprint ,current_app
from datetime import datetime,timedelta
from app import db 
from app.model import User
import jwt
from app.util import  email_check , user_check ,set_password 
from app.dob import  insert_user

auth=Blueprint("/auth",__name__)
@auth.route('/login', methods =['POST'])
def login():
    json_body = request.get_json()    
    if request.method == 'POST':
           userpassword = json_body['userpassword']
           
           email = json_body['email'] 
           check_email=db.session.query(User).filter_by(email=email).first()           
           if check_email is None:
               return jsonify({'msg':"Signup Please"})
               
           else:                  
               token = jwt.encode({'public_id': 1,'exp' :str( datetime.utcnow() + timedelta(minutes = 30)) }, current_app.config.get('SECRET_KEY'))
               return jsonify(message="Login successfully", access_token=token)
               
     
auth=Blueprint("/auth",__name__)
@auth.route('/signup', methods =['POST'])
def singup():
    json_body = request.get_json()
    username = json_body['username']
    email = json_body['email']
    userpassword = json_body['userpassword']
    confirmpwd = json_body['confirmpwd']
    
    email_ans=email_check(email)
    user_ans=user_check(username)
    if email_ans==True and user_ans==True :
        if confirmpwd == userpassword:   
            hash_password=set_password(userpassword)    
            msg=insert_user(email,hash_password,username)
            return jsonify({"msg": msg})
    else :
      msg="Please enter a valid email address"
      return jsonify({"message  ": msg})    
           

 
    

