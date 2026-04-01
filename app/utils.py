from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from app import models
from app.models import Student
from sqlalchemy.orm import session
from app.deps import get_db
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException,status

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="userauthentication/login")

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30



def hashpassword(password:str)->str:
    pwd=PasswordHash.recommended()
    return pwd.hash(password)

def verifypassword(password:str,hashedpassword:str)->bool:
    pwd=PasswordHash.recommended()
    return pwd.verify(password,hashedpassword)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def authentictateuser(db,studentemail:str,password:str):
    user=db.query(models.Student).filter(models.Student.studentemail==studentemail).first()
    if not user:
        return False
    if not verifypassword(password,user.password):
        return False
    return user

def get_current_user(token: str = Depends(oauth2_scheme),db: session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")

        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user=db.query(Student).filter(Student.studentemail == email).first()

        return user

    except JWTError:
        raise HTTPException(status_code=401, detail="Token error")
