from app import ma 
class UserSchema(ma.Schema):
      class Meta:
            fields=('id','password','email','role_id')

class RoleSchema(ma.Schema):
      class Meta:
            fields=('id','userole')


