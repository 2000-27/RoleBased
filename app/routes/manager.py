from flask import request , jsonify ,current_app,Blueprint
import jwt 
from app.dob import insert_into_db
from app.util import role
Manager=Blueprint("/Manager/data",__name__)
def token_access(f):
      def decorator(*args, **kwargs):
            payload=request.headers["Authorization"]
            try:
                  payload = payload.split(" ")[1]
                  decoded_jwt=jwt.decode(payload, current_app.config.get('SECRET_KEY'), algorithms=["HS256"])
                  role_name=role(decoded_jwt)
                  if role_name !="MANAGER":
                        return jsonify({"message": " Only manager can access!!!"})
                                          
            except  :
                    return jsonify({"message": "Invalid token!"})
            return f(role_name, *args, **kwargs)
      return decorator     
               
   
@Manager.route('/Manager/data', methods =['POST'])
@token_access
def  manager(current_user):
    msg=insert_into_db()
    return jsonify({"msg":msg})
    



         
            
            

            
 