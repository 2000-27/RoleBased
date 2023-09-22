from flask import request , jsonify ,current_app,Blueprint
import jwt 
from app import db
from app.model import User,Role
Admin=Blueprint("/Admin",__name__)

def token_access(f):
   @wraps(f)
   def decorator(*args, **kwargs):
         print("heelo")


@token_access
@Admin.route('/admins', methods =['POST'])
def  admins():
         msg=''
         payload=request.headers["Authorization"]
         try:
            payload = payload.split(" ")[1]
            decoded_jwt=jwt.decode(payload, current_app.config.get('SECRET_KEY'), algorithms=["HS256"])
            user_id=decoded_jwt['user_id']
            user_role_id=decoded_jwt['user_role_id']
            print('user_role_id',user_role_id)
            print('user_id',user_id)
            roles=db.session.query(Role).filter_by(id=user_role_id).first() 

            if roles.role_name=='ADMIN':
                     print("you can change the info")
                     return jsonify("you can change the info")
            

            
            
            else: 
                   print("You cann't access")
         except Exception as err:
               msg="you can't access these page "  
               print("your error is ",err)
               return jsonify({"message  ": msg})    
             
  