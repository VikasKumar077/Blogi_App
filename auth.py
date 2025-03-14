from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from models import User
from database import get_session
import os

import jwt, bcrypt, datetime


SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM= os.getenv("ALGORITHM")
router = APIRouter()





def create_token(user):
    payload = { "sub": str(user.id),                  
        "username": user.username, # Include username in token
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/register/")
def register(user: User, session: Session = Depends(get_session)):
    existing_user = session.exec(select(User).where(User.username == user.username)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed_password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt()).decode()
    user.password = hashed_password
    session.add(user)
    session.commit()
    return {"message": "User registered successfully"}

@router.post("/login/")
def login(user: User, session: Session = Depends(get_session)):
    db_user = session.exec(select(User).where(User.username == user.username)).first()
    if not db_user or not bcrypt.checkpw(user.password.encode(), db_user.password.encode()):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(db_user)
    return {"token": token,"username": db_user.username}
