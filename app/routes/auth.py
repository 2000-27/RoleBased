from flask import request , jsonify , Blueprint ,current_app
from datetime import datetime,timedelta
from app import db 
from app.model import User
import jwt
from app.dob import  insert_into_db
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
    msg=insert_into_db()
    print("your error is ",msg)
    return jsonify({"msg":msg})


  






       

       