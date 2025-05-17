from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from gumigest_app.core.deps import get_db
from gumigest_app.schemas.user import UserCreate, UserOut
from gumigest_app.crud.user import create_user, verify_user_password, get_user_by_username
from gumigest_app.core.database import SessionLocal
from gumigest_app.core.security import hash_password
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta, datetime
from jose import JWTError, jwt

router = APIRouter()


@router.get("/users/{username}", response_model=UserOut)
def read_user(username: str, db: Session = Depends(get_db)) -> any:
    user = get_user_by_username(db, username)
    if not user:
        raise HTTPException(status=404, detail="User not found")
    return user
