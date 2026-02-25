from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class StuCreate(BaseModel):
    name:str
    age:int=Field(gt=0)
    email:EmailStr
    password:str=Field(min_length=6,max_length=12)
    dept:Optional[str]=None
    ph_no:str=Field(min_length=10,max_length=10)

class StuUpdate(BaseModel):
    name:str
    age:int=Field(gt=0)
    email:EmailStr
    password:str=Field(min_length=6,max_length=12)
    dept:Optional[str]=None
    ph_no:str=Field(min_length=10,max_length=10)

class StuResponse(BaseModel):
    name:str
    email:EmailStr
    ph_no:str=Field(min_length=10,max_length=10)

    class config:
        orm_mode=True
