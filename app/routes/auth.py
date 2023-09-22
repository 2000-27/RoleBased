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
           check_user=db.session.query(User).filter_by(email=email).first()           
           if check_user is None:
               return jsonify({'msg':"Signup Please"})                
           else:  
               role_id=check_user.role_id
               user_id=check_user.id
               
               token = jwt.encode({'user_role_id': str(role_id),'user_id': str(user_id), 'exp' :  datetime.utcnow() + timedelta(minutes = 30) }, current_app.config.get('SECRET_KEY'))   
                
               return jsonify(message="Login successfully" , access_token=token)
               
     

@auth.route('/signup', methods =['POST'])
def singup():
    json_body = request.get_json()
    username = json_body['username']
    email = json_body['email']
    userpassword = json_body['userpassword']
    confirmpwd = json_body['confirmpwd']
    email_ans=email_check(email)
    user_ans=user_check(username)
    if confirmpwd != userpassword: 
             msg="Password and confirm password should be same"
             return jsonify({"message  ": msg})  
                
    else:
         if email_ans ==True:
               if  user_ans==True :
                    hash_password=set_password(userpassword)    
                    msg=insert_user(email,hash_password,username)
                    return jsonify({"msg": msg})
               else:
                    msg="Please enter a valid username"
                    return jsonify({"message  ": msg})  
         else :
                msg="Please enter a valid email address"
                return jsonify({"message  ": msg})    
             
        
    


  






       

       