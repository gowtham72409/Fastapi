from sqlalchemy import Column,Integer,String
from database import Base

class Student(Base):
    __tablename__="student"
    stu_id=Column(Integer,primary_key=True,index=True)
    name=Column(String,unique=True,index=True)
    age=Column(Integer)
    email=Column(String,unique=True,index=True)
    password=Column(String)
    dept=Column(String)
    ph_no=Column(String,unique=True,index=True)
    
