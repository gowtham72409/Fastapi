from sqlalchemy import Column,Integer,String
from database import Base

class User(Base):
    __tablename__="user"

    user_id=Column(Integer,primary_key=True,index=True)
    user_name=Column(String(50),unique=True,index=True)
    email=Column(String(50),unique=True)
    password=Column(String(15))
    ph_no=Column(String(10),unique=True)
