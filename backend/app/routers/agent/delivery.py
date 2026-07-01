from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user

from app.models.order import Order
from app.models.agent import Agent
from app.models.user import User

from app.schemas.tracking import TrackingUpdate

from app.services.tracking_service import TrackingService

from app.utils.constants import (
    OrderStatus,
    UserRole,
)

router = APIRouter(
    prefix="/agent/orders",
    tags=["Agent Delivery"],
)


def validate_agent_order(
    db: Session,
    current_user: User,
    order_id: int,
):
    """
    Validate that:
    1. Current user is an agent
    2. Agent profile exists
    3. Order exists
    4. Order belongs to the current agent
    """

    if current_user.role != UserRole.AGENT:
        raise HTTPException(
            status_code=403,
            detail="Only agents can access this endpoint",
        )

    agent = (
        db.query(Agent)
        .filter(Agent.user_id == current_user.id)
        .first()
    )

    if agent is None:
        raise HTTPException(
            status_code=404,
            detail="Agent profile not found",
        )

    order = (
        db.query(Order)
        .filter(Order.id == order_id)
        .first()
    )

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )

    if order.agent_id != agent.id:
        raise HTTPException(
            status_code=403,
            detail="This order is not assigned to you.",
        )

    return order


# ------------------------------
# Get Assigned Orders
# ------------------------------

@router.get("")
def get_my_orders(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    if current_user.role != UserRole.AGENT:
        raise HTTPException(
            status_code=403,
            detail="Only agents can access this endpoint",
        )

    agent = (
        db.query(Agent)
        .filter(Agent.user_id == current_user.id)
        .first()
    )

    if agent is None:
        raise HTTPException(
            status_code=404,
            detail="Agent profile not found",
        )

    return (
        db.query(Order)
        .filter(Order.agent_id == agent.id)
        .all()
    )


# ------------------------------
# Pickup
# ------------------------------

@router.put("/{order_id}/pickup")
def pickup_order(
    order_id: int,
    body: TrackingUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    validate_agent_order(
        db,
        current_user,
        order_id,
    )

    return TrackingService.update_status(
        db=db,
        order_id=order_id,
        user_id=current_user.id,
        new_status=OrderStatus.PICKED_UP,
        remarks=body.remarks,
    )


# ------------------------------
# Transit
# ------------------------------

@router.put("/{order_id}/transit")
def transit_order(
    order_id: int,
    body: TrackingUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    validate_agent_order(
        db,
        current_user,
        order_id,
    )

    return TrackingService.update_status(
        db=db,
        order_id=order_id,
        user_id=current_user.id,
        new_status=OrderStatus.IN_TRANSIT,
        remarks=body.remarks,
    )


# ------------------------------
# Delivered
# ------------------------------

@router.put("/{order_id}/deliver")
def deliver_order(
    order_id: int,
    body: TrackingUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    validate_agent_order(
        db,
        current_user,
        order_id,
    )

    return TrackingService.update_status(
        db=db,
        order_id=order_id,
        user_id=current_user.id,
        new_status=OrderStatus.DELIVERED,
        remarks=body.remarks,
    )