from flask import request,jsonify,Blueprint
from app.util import email_check,user_check
from app.dob import insert_user
second=Blueprint("/second",__name__)

@second.route('/signup', methods =['POST'])
def singup():
    json_body = request.get_json()
    msg = ''
    username = json_body['username']
    email = json_body['email']
    userpassword = json_body['userpassword']
    roles=json_body['roles']
    email_ans=email_check(email)
    user_ans=user_check(username)
    if email_ans==True and user_ans==True:     
          msg=insert_user(email,userpassword,username,roles)
          return jsonify({"msg": msg})
    else :
            msg="!! ENTER THE CORRECT EMAIL !!!"
            return jsonify({"message  ": msg})    
              

 
    

