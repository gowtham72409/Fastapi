from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
import models
import schemas
from database import engine,SessionLocal

models.Base.metadata.create_all(bind=engine)

# Looks at all models that inherit from Base
# Creates tables in database
# Uses engine connection

app=FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Creates a new database session
# Gives it to endpoint
# Closes it after request finishes
# Think of it like:
# Open connection → use → close connection

db:Session=Depends(get_db)

# FastAPI automatically:
# Calls get_db()
# Injects db into function
# Closes session after request.This is called Dependency Injection

@app.post("/user",response_model=schemas.UserResponse)

# When client sends POST request to /users
# Use UserResponse schema for output

def create(user:schemas.UserCreate,db:Session=Depends(get_db)):
    db_user=models.User(email=user.email,password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Create SQLAlchemy object
# Add to session
# Commit (save permanently)
# Refresh (get generated id)
# Even though we return full object, response_model removes password automatically.

@app.get("/user")
def get_user(db:Session=Depends(get_db)):
    return db.query(models.User).all()

@app.put("/user/{id}",response_model=schemas.UserResponse)
def update_user(id:int,user:schemas.UserUpdate,db:Session=Depends(get_db)):
    db_user=db.query(models.User).filter(models.User.id==id).first()
    if not db_user:
        return {"error": "User not found"}
    db_user.email=user.email
    db_user.password=user.password
    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/user/{id}")
def delete_user(id:int,db:Session=Depends(get_db)):
    db_user=db.query(models.User).filter(models.User.id==id).first()
    if not db_user:
        return {"error":"User not found"}
    db.delete(db_user)
    db.commit()
    return {"message":"User delete successfully"}