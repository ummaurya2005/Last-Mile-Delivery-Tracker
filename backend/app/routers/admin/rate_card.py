from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_admin

from app.schemas.rate_card import (
    RateCardCreate,
    RateCardResponse,
)

from app.services.admin_service import AdminService

router = APIRouter(
    prefix="/admin/rate-cards",
    tags=["Admin - Rate Cards"],
)


@router.post(
    "",
    response_model=RateCardResponse,
    status_code=201,
)
def create_rate_card(
    rate: RateCardCreate,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin),
):

    try:
        return AdminService.create_rate_card(
            db,
            rate,
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get(
    "",
    response_model=list[RateCardResponse],
)
def get_rate_cards(
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin),
):

    return AdminService.get_all_rate_cards(db)