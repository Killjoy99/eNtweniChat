from fastapi import APIRouter, Depends, HTTPException, status

from .models import (
    UserLogin,
    UserLoginResponse,
    UserRead,
    UserRegister,
    UserRegisterResponse,
    UserCreate,
    UserUpdate,
)

from .service import get, get_by_phone_number, update, create

auth_router = APIRouter()
user_router = APIRouter()

@user_router.post("", response_model=UserRead,)
async def create_user(user_in: UserCreate, db_session: DbSession):
    """ Creates a new user"""
    user = get_by_phone_number(db_session=db_session, phone_number=user_in.phone_number)
    if not user:
        user = create(db_session=db_session, user_in=user_in)
        return user
    else:
        print(f"Phone number already registered: {user_in}")
        return
    