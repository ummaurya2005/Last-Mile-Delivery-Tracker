from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_current_user
from app.models.user import User
from app.database import get_db
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.user import (
    UserCreate,
    UserLogin,
    UserResponse,
    TokenResponse,
)

from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):

    try:
        return AuthService.register_user(
            db,
            user,
        )

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):

    result = AuthService.login_user(
        db,
        form_data.username,   # OAuth2 uses username field
        form_data.password,
    )

    if result is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Email or Password"
        )

    return {
        "access_token": result["access_token"],
        "token_type": result["token_type"],
    }

@router.get(
    "/me",
    response_model=UserResponse
)
def get_me(
    current_user: User = Depends(get_current_user)
):
    return current_user