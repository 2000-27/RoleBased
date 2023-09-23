from flask import request , jsonify ,current_app,Blueprint
import jwt 
from app.util import role

from app.dob import insert_into_db
Admin=Blueprint("/Admin/data",__name__)
def token_access(f):
      def decorator(*args, **kwargs):
            payload=request.headers["Authorization"]
            try:
                  payload = payload.split(" ")[1]
                  decoded_jwt=jwt.decode(payload, current_app.config.get('SECRET_KEY'), algorithms=["HS256"])
                  role_name=role(decoded_jwt)
                  if role_name !="ADMIN":
                        return jsonify({"message": " Only admin can access!!!"})
                                          
            except  Exception as err:
                  print("your error is ",err)
                  return jsonify({"message": "Invalid token!"})
            return f(role_name, *args, **kwargs)
      return decorator     
               
   
@Admin.route('/Admin/data', methods =['POST'])
@token_access
def  admins(current_user):
    msg=insert_into_db()
    return jsonify({"msg":msg})
    



         
            
            

            
 