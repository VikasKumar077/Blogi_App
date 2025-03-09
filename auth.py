from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from models import User
from database import get_session

import jwt, bcrypt, datetime

SECRET_KEY = "3f8e1f8b9c5a4c1b2f6e8d7f6b5a4c3d8e1f9b6a7c5e4d3f2a1b0c9e8d7f6b5a"
router = APIRouter()





def create_token(user):
    payload = { "sub": str(user.id),                  
        "username": user.username, # Include username in token
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

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
