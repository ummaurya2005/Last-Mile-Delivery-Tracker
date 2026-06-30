from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.zone import (
    ZoneCreate,
    ZoneResponse,
)

from app.services.admin_service import AdminService

from app.dependencies import get_current_admin


router = APIRouter(
    prefix="/admin/zones",
    tags=["Admin - Zones"]
)


@router.post(
    "",
    response_model=ZoneResponse,
    status_code=201,
)
def create_zone(
    zone: ZoneCreate,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):

    try:

        return AdminService.create_zone(
            db,
            zone,
        )

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get(
    "",
    response_model=list[ZoneResponse],
)
def get_zones(
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):

    return AdminService.get_all_zones(db)