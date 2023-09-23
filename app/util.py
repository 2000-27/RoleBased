from werkzeug.security import generate_password_hash ,check_password_hash
import re 
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