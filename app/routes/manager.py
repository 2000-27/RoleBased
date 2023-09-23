from flask import request , jsonify , Blueprint
from app.dob import insert_into_db
from app.util import token_access
manager_mp=Blueprint("/create",__name__)
   
@manager_mp.route('/create', methods =['POST'])
@token_access
def  create(user_id,role_id):
    print("your role id is ",role_id)
    if role_id is not "2":
       msg="You are not authorized  "
       return jsonify({"msg":msg})
    else:
        json_body = request.get_json()
        username = json_body['username']
        email = json_body['email']
        userpassword = json_body['userpassword']
        confirmpwd = json_body['confirmpwd']
        role_id=json_body['role_id']
        msg=insert_into_db(username,email,userpassword,confirmpwd,role_id)
        return jsonify({"msg":msg})
        


      
            
            

            
 