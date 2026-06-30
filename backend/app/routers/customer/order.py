from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.dependencies import get_current_user

from app.models.user import User

from app.schemas.order import (
    OrderCreate,
    OrderResponse,
)

from app.services.order_service import OrderService

router = APIRouter(
    prefix="/customer/orders",
    tags=["Customer Orders"],
)


@router.post(
    "",
    response_model=OrderResponse,
    status_code=201,
)
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return OrderService.create_order(
        db,
        current_user,
        order,
    )


@router.get(
    "",
    response_model=list[OrderResponse],
)
def get_orders(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return OrderService.get_customer_orders(
        db,
        current_user,
    )