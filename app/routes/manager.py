from flask import request , jsonify , Blueprint 
from app.dob import insert_into_db 
from app.util import token_required , admin_required
manager_mp=Blueprint("/create",__name__)
@manager_mp.route('/create', methods =['POST'])

@token_required
def create(user_id,user_role_id,decode):
        role_name=admin_required(decode) 
        print("your role name is ",role_name)
        json_body = request.get_json()
        username = json_body['username']
        email = json_body['email']
        userpassword = json_body['userpassword']
        confirmpwd = json_body['confirmpwd']
        role_id=json_body['role_id']
        msg=insert_into_db(username,email,userpassword,confirmpwd,role_id)
        return jsonify({"msg":msg})
        


      
      
            
            

            
 