from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True)
    studentname = Column(String)
    studentage=Column(Integer)
    studentemail=Column(String)
    password=Column(String)
    
