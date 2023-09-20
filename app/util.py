import re 

def email_check(email):
    if not re.match(r'[^@]+@[^@]+\.[^@]+',email):  
           msg = 'INVALID EMAIL ADDRESS !!!!'
    else :
          msg =True
    return msg       
    
def user_check(username):
        if not (re.match(r'[a-zA-Z0-9\s]+$',username)): 
           msg = 'Username must contain only characters , digit  and space !!!!!'    
        else:
           msg=True   
        return msg

