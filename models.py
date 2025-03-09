from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class Post(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    content: str
    author: str
    is_public: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.now)
    last_updated: datetime = Field(default_factory=datetime.now)

    
    

class User(SQLModel, table=True):
    __tablename__ = "users" 
    id: int = Field(default=None, primary_key=True)
    name: str
    username: str = Field(unique=True)
    password: str