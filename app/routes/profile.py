from flask import request , jsonify , Blueprint ,current_app
import jwt
from app.model import User,Role
from app import db

profiles=Blueprint("/profile",__name__)
@profiles.route('/userprofile', methods =['GET'])
def  userprofile():
         msg=''
         payload=request.headers["Authorization"]
         try:
            payload = payload.split(" ")[1]
            decoded_jwt=jwt.decode(payload, current_app.config.get('SECRET_KEY'), algorithms=["HS256"])
            user_id=decoded_jwt['user_id']
            user_role_id=decoded_jwt['user_role_id']
            check_user=db.session.query(User).filter_by(id=user_id).first()  
            roles=db.session.query(Role).filter_by(id=user_role_id).first()  
            current_user = {'name': check_user.username, 'email': check_user.email, 'Id': check_user.id,"role":roles.role_name}
            return jsonify(current_user) 
         except Exception as err:
               msg="Please login"  
               return jsonify({"message  ": msg})    
             
  