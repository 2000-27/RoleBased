from flask import request , jsonify , Blueprint ,current_app
from datetime import datetime,timedelta
from app import db 
from app.model import User
import jwt

Login=Blueprint("/Login",__name__)
@Login.route('/login', methods =['POST'])
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
               
     

