from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from database import SessionLocal,engine
import models
import schemas
from until import hash_password,verify_password

models.Base.metadata.create_all(bind=engine)
app=FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db:Session=Depends(get_db)

@app.put("/stu",response_model=schemas.StuResponse)
def create(student:schemas.StuCreate,db:Session=Depends(get_db)):
    db_stu=models.Student(name=student.name,age=student.age,email=student.email,password=student.password,
                         dept=student.dept,ph_no=student.ph_no )
    
    db.add(db_stu)
    db.commit()
    db.refresh(db_stu)
    return db_stu

@app.get("/stu")
def retrive(db:Session=Depends(get_db)):
    return db.query(models.Student).all()

@app.put("/stu/{stu_id}",response_model=schemas.StuResponse)
def update(stu_id:int,student:schemas.StuUpdate,db:Session=Depends(get_db)):
    db_stu=db.query(models.Student).filter(models.Student.stu_id==stu_id).first()
    if not db_stu:
        return {"Error: Student not found"}
    db_stu.name=student.name
    db_stu.age=student.age
    db_stu.email=student.email
    db_stu.password=student.password
    db_stu.dept=student.dept
    db_stu.ph_no=student.ph_no
    db.commit()
    db.refresh(db_stu)
    return db_stu

@app.delete("/stu/{stu_id}")
def delete(stu_id:int,db:Session=Depends(get_db)):
    db_stu=db.query(models.Student).filter(models.Student.stu_id==stu_id).first()
    if not db_stu:
        return {"error":"User not found"}
    db.delete(db_stu)
    db.commit()
    return {"message":"User delete successfully"}
