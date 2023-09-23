from werkzeug.security import generate_password_hash ,check_password_hash
from flask import request , jsonify , current_app ,abort
import re , jwt  
from app import db
from app.model import Role
def email_check(email):
    if not re.match(r'[^@]+@[^@]+\.[^@]+',email):  
           return False
    else :
          return True
        
    
def user_check(username):
        if not (re.match(r'[a-zA-Z0-9\s]+$',username)): 
            return False
        else :
          return True    


def set_password(password):
        password_hash = generate_password_hash(password)
        return password_hash



def role(decoded_jwt):
       user_role_id=decoded_jwt['user_role_id']
       roles=db.session.query(Role).filter_by(id=user_role_id).first() 
       return roles.role_name 



def token_required(f):
      def decorator(*args, **kwargs):
            payload=request.headers["Authorization"]
            try:
                  payload = payload.split(" ")[1]
                  decoded_jwt=jwt.decode(payload, current_app.config.get('SECRET_KEY'), algorithms=["HS256"])
                  user_id=decoded_jwt['user_id']
                  user_role_id=decoded_jwt['user_role_id']
               
            except  Exception as err:
                  print("your error is ",err)
                  return jsonify({"message": "Invalid token!"})
            return f(user_id,user_role_id,decoded_jwt, *args, **kwargs)
      return decorator     
  


def admin_required(decoded_jwt):
      user_role_id=decoded_jwt['user_role_id']
      user_role_id=decoded_jwt['user_role_id']
      roles=db.session.query(Role).filter_by(id=user_role_id).first() 
      role_name=roles.role_name  
      if role_name == "USER":
            abort(401)
      return role_name  


