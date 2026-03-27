from pydantic import BaseModel,Field,EmailStr
from typing import Annotated,Literal
from typing import Optional, Any, List


class APIresponse(BaseModel):
    message:str
    data:Optional[Any]=None


class addstudentschema(BaseModel):
    studentname:str
    studentage:int
    studentemail:EmailStr
    password:str


class addstudentresponse(BaseModel):
    studentname:str
    studentage:int
    studentemail:str
    
    class Config:
        from_attributes = True 

class studentdetailbyidschema(BaseModel):
    studentname:str
    studentage:int
    studentemail:str

class getallstudetentdetailresponseschema(BaseModel):
    studentname:str
    studentage:int 
    studentemail:str
    
    class Config:
        from_attributes = True 

class updatestudentdetailschema(BaseModel):
    studentname:str
    studentage:int

