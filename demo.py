from fastapi import FastAPI
from  pydantic import BaseModel,EmailStr,Field,field_validator
from typing import Optional

app=FastAPI()


# get method
# get method is retrive data from server and data visible in URL path

@app.get("/home")
def home():
    return {"message":"Hello world"}


# path parameter
# path paramater is value inside the URL path and chane dynamicllly
# required part is url

@app.get("/user/{user_id}")
def user(user_id:int):
    return {"user_id":user_id}

# Query parameter
# It is used to extra information added to URL path after "?" to filter or customize result
# optional extra info

@app.get("users")
def users(q:str):
    return {"Query":q}

# Post 
# it is send date to server and not visible in URL path

class Student(BaseModel):
    name:str
    age:int

@app.post("student")
def detial(detials:Student):
    return detials

# Pydantic Model
# Pydantic model is data validation,data structure and automatically check data type
# we can import basemodel from pydantic
# Pydantic model is a data validation class used in FastAPI to define 
# and validate request and response data.

class User(BaseModel):
    name:str
    age:int=Field(gt=0)
    dept:Optional[str]=None
    email:EmailStr
    password:int= Field(min_length=6,max_length=9)

@app.post("/user")
def users(user:User):
    return user

class Login(BaseModel):
    email:EmailStr
    password:str

@field_validator("password")
def passworsd_len(cls,v):
    if len(v)<6:
        raise ValueError("Password is too short")
    return v

@app.post("/login")
def login(data:Login):
    return {"email":data.email,"password":data.password}


# ORM -object relational mapping
# When using SQLAlchemy (database models), FastAPI needs help converting 
# database objects into JSON

# SQLAlchemy Model → talks to database

# Pydantic Schema → validates API data

# orm_mode → connects both

# FastAPI → connects everything

# Dependency Injection
# Dependency Injection (DI) is a design pattern where a function or class does not 
# create its own dependencies, but instead receives them from an external source.

def config():
    orm_mode=True

# why use ?-> Because by default pydantic expect dictionary data,But SQLAlchemy 
# returns object data, not dictionary.so use orm is convert database object to json

# what is json

# #JSON = JavaScript Object Notation
# It is a lightweight data exchange format used to send and receive data between:
# Client (Frontend / Postman)
# Server (Backend like FastAPI)

# Authentication JWT

# Authentication is the process of verifying who the user is.
# In backend systems (like FastAPI), authentication ensures:

# Authentication → Verifies identity (Who are you?)
# Authorization → Verifies permission (What can you access?

# Common Authentication Methods in FastAPI
# 1️⃣ Basic Authentication

# Username + password sent in every request (not secure for production)

# 2️⃣ JWT Authentication (Most Common)

# Uses JSON Web Tokens
# Stateless authentication
# Used in modern APIs

# 3️⃣ OAuth2 Authentication

# Industry standard protocol
# Used with JWT

# Authentication in FastAPI =Verifying user identity using credentials and 
# tokens before allowing access to protected endpoints

# JWT-json web token
# JWT is a secure, compact token format used for authentication and authorization 
# by digitally signing JSON data to verify user identity.three part

# header,payload,signature
# Header contain alogithm and tokens (eg..{"alg":"HS256","typ":"JWT"})
# Payload contain user data {"sub": "gowtham@gmail.com","exp": 170000000 }
# sub → subject (user identifier)
# exp → expiration time
# iat → issued at
# signature create header+payload+screate token ,it ensurs not modified the token