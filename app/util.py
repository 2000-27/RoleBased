from werkzeug.security import generate_password_hash
import re 

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
        print("your password is ",password)
        print("your hash password is ",password_hash)
        return password_hash