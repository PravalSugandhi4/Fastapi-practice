
from .schema import *
from fastapi import FastAPI, Depends,Query
from sqlalchemy.orm import Session
from .deps import get_db
from app.models import Student
from app.models import Base
from app.database import engine
from app.dboperations import *
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/",tags=["DB connection test"])
def test_db(db: Session = Depends(get_db)):
    return {"message": "DB Connected Successfully"}

@app.post('/addstudentdata/',response_model=addstudentresponse,tags=["normal API"])
def addstudentdata(request:addstudentschema,db:Session=Depends(get_db)):
    return addstudent(db,request)

@app.get("/getdetailbyid/{studentid}",response_model=studentdetailbyidschema)
def studentdetail(studentid:int,db:Session=Depends(get_db)):
    return studentdetailbyid(db,studentid)


@app.get("/detallstudentdata/",response_model=List[getallstudetentdetailresponseschema])
def getallstudentdata(page:int=Query(1,gt=0),limit:int=Query(10,gt=1), db:Session=Depends(get_db)):
    skip = (page - 1) * limit
    return getallstudentdetail(db,skip,limit)
 
    
@app.put('/updatestudentdetailbyid/{studentid}',status_code=200)
def updatestudentdata(studentid:int,data:updatestudentdetailschema,db:Session=Depends(get_db)):
    return updatestudentdetail(studentid,db,data)