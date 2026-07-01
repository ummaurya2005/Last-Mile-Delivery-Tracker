from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.tracking import TrackingResponse

from app.services.tracking_service import TrackingService

router = APIRouter(
    prefix="/tracking",
    tags=["Tracking"],
)


@router.get(
    "/{order_id}",
    response_model=list[TrackingResponse],
)
def get_tracking(
    order_id: int,
    db: Session = Depends(get_db),
):

    return TrackingService.get_tracking_history(
        db,
        order_id,
    )