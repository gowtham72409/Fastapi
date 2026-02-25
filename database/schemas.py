from pydantic import BaseModel,EmailStr

class UserCreate(BaseModel):
    email:EmailStr
    password:str

# This is used when creating a user.

class UserUpdate(BaseModel):
    email:EmailStr
    password:str

class UserResponse(BaseModel):
    id:int
    email:EmailStr

# This controls what we send BACK to client.
    class config:
        orm_mode=True



# This is required in Pydantic v2.
# Why?
# Because SQLAlchemy returns an object like
# Pydantic must know how to read attributes from that object.
# from_attributes = True allows that