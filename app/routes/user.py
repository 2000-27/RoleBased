from flask import  jsonify , Blueprint 
from app.util import token_required
from app.model import User,Role
from app import db

user_profiles=Blueprint("profile",__name__)
@user_profiles.route('/profile', methods =['GET'])
@token_required
def  userprofile(user_id,user_role_id):
        check_user=db.session.query(User).filter_by(id=user_id).first()  
        roles=db.session.query(Role).filter_by(id=user_role_id).first()  
        current_user = {'name': check_user.username , 'email': check_user.email , 'Id': check_user.id ,"role":roles.role_name}
        return jsonify(current_user) 
       
             
  