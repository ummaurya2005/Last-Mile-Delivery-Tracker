from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)


class AuthService:

    @staticmethod
    def register_user(
        db: Session,
        user: UserCreate,
    ):

        existing_user = (
            db.query(User)
            .filter(User.email == user.email)
            .first()
        )

        if existing_user:
            raise Exception("Email already exists")

        db_user = User(
            name=user.name,
            email=user.email,
            password=hash_password(user.password),
            role=user.role,
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    @staticmethod
    def login_user(
        db: Session,
        email: str,
        password: str,
    ):

        user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if not user:
            return None

        if not verify_password(
            password,
            user.password,
        ):
            return None

        access_token = create_access_token(
            {
                "sub": str(user.id),
                "role": user.role,
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": user,
        }