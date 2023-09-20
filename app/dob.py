from app import db
from app.schema import RoleSchema
from app.model import Role,User
def insert_user(email,password,username,roles):
    msg=''
    role_id=0
    check_role=db.session.query(Role).filter_by(role_name=roles).first()
    check_email=db.session.query(User).filter_by(email=email).first()
    check_password=db.session.query(User).filter_by(password=password).first()    
    if check_role ==None  :
       msg="ENTER THE CORRECT ROLES"
    elif  check_email!=None  or check_password !=None:
        msg="USER IS ALREADY EXIT"      
    else : 
        if roles=="admin":
            role_id=3
        elif  roles =="User":
            role_id=4
        elif  roles =="manager":
                role_id=2
    
        new_User=User(email,password,role_id)
        db.session.add(new_User)
        db.session.commit()         
        msg="DATA IS INSERTED SUCCESSFULLY"
    
    return msg

# def insert_role(new_role):
#     print("your new role is ",new_role)
#     Single_user=RoleSchema()
#     db.session.add(new_role)
#     db.session.commit()
#     return Single_user.jsonify(new_role)
