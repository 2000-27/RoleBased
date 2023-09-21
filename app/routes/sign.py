from flask import request , jsonify , Blueprint
from app.util import  email_check , user_check
from app.dob import  insert_user

sign=Blueprint("/sign",__name__)
@sign.route('/signup', methods =['POST'])
def singup():
    json_body = request.get_json()
    username = json_body['username']
    email = json_body['email']
    userpassword = json_body['userpassword']
    email_ans=email_check(email)
    user_ans=user_check(username)
    if email_ans==True and user_ans==True:     
          msg=insert_user(email,userpassword,username)
          return jsonify({"msg": msg})
    else :
      msg="Invalid Email Format"
      return jsonify({"message  ": msg})    
           

 
    

