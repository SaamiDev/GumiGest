from email.policy import default
from enum import unique
from operator import index

from sqlalchemy import Columnm, Integer, String, Boolean, nullsfirst
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Columnm(Integer, primary_key=True, index=True)
    username = Columnm(String(50), unique=True, index=True, nullable=False)
    hashed_password = Columnm(String(255), nullable=False)
    is_active = Columnm(Boolean, default=True)