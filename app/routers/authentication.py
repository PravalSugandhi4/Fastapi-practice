
from datetime import timedelta
from fastapi import APIRouter
from app.schema import loginschema,loginschemaresponse,Token,TokenData
from app.utils import authentictateuser
from app.deps import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import HTTPException,status
from app.utils import create_access_token,get_current_user
from fastapi.security import OAuth2PasswordRequestForm


router=APIRouter(tags=["Authentication APIs"],prefix="/userauthentication")

@router.post("/login")
def loginuser(data: OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    user=authentictateuser(db,data.username,data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid email or password")
    token=create_access_token(data={"sub":user.studentemail},expires_delta=timedelta(minutes=30))
    
    return {
        "access_token":token,
        "token_type":"bearer"
    }
@router.get("/userprofile",response_model=loginschemaresponse)
def get_me(user: str = Depends(get_current_user)):
    return user
