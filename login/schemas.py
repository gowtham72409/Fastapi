from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class UserCreate(BaseModel):
    user_name:str
    email:EmailStr
    password:str=Field(min_length=6,max_length=72)
    ph_no:str=Field(min_length=10,max_length=10)

class UserLogin(BaseModel):
    email:EmailStr
    password:str=Field(min_length=6,max_length=72)

class Token(BaseModel):
    access_token:str
    token_type:str