from app.schema import *
from fastapi import Depends,Query
from sqlalchemy.orm import Session
from app.deps import get_db
from app.dboperations import *
from typing import List 
from fastapi import APIRouter


router = APIRouter(tags=["Student APIs"],prefix=
                   "/studentapi")

# @router.get("/",tags=["DB connection test"])
# def test_db(db: Session = Depends(get_db)):
#     return {"message": "DB Connected Successfully"}

@router.post('/addstudentdata/',response_model=addstudentresponse,status_code=201)
def addstudentdata(request:addstudentschema,db:Session=Depends(get_db)):
    return addstudent(db,request)

@router.get("/getdetailbyid/{studentid}",response_model=studentdetailbyidschema)
def studentdetail(studentid:int,db:Session=Depends(get_db)):
    return studentdetailbyid(db,studentid)


@router.get("/detallstudentdata/",response_model=List[getallstudetentdetailresponseschema])
def getallstudentdata(page:int=Query(1,gt=0),limit:int=Query(10,gt=1), db:Session=Depends(get_db)):
    skip = (page - 1) * limit
    return getallstudentdetail(db,skip,limit)
 
    
@router.put('/updatestudentdetailbyid/{studentid}',status_code=200)
def updatestudentdata(studentid:int,data:updatestudentdetailschema,db:Session=Depends(get_db)):
    return updatestudentdetail(studentid,db,data)