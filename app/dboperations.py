from app.models import *
from app.schema import *
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.utils import hashpassword

def addstudent(db,data):
    instance=db.query(Student).filter(Student.studentemail==data.studentemail).first()
    if instance:
        raise HTTPException(status_code=409,detail="student with this email alrady exist")
    instance=Student(studentname=data.studentname,studentemail=data.studentemail,studentage=data.studentage,password=hashpassword(data.password))
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance

def studentdetailbyid(db,data):
    instance=db.query(Student).filter(Student.id==data).first()
    if not instance:
        raise HTTPException(status_code=404,detail="No student with this id exist")
    return instance

def getallstudentdetail(db,start,end):
    instance=db.query(Student).offset(start).limit(end).all()
    return instance 

def updatestudentdetail(id,db,data):
     instance=db.query(Student).filter(Student.id==id).first()
     if not instance:
        raise HTTPException(status_code=404,detail="No student with this id exist")
     instance.studentname = data.studentname
     instance.studentage = data.studentage
     db.commit()
     db.refresh(instance)
     return {"Message":"Data updated sucessfully"}
     
    
