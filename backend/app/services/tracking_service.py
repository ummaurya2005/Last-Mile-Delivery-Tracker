from sqlalchemy.orm import Session

from app.models.order import Order
from app.models.agent import Agent
from app.models.tracking import TrackingHistory

from app.utils.constants import (
    OrderStatus,
    AgentStatus,
)


class TrackingService:

    @staticmethod
    def add_tracking(
        db: Session,
        order_id: int,
        status: str,
        updated_by: int,
        remarks: str = None,
    ):
        """
        Create a tracking history record.
        """

        history = TrackingHistory(
            order_id=order_id,
            status=status,
            updated_by=updated_by,
            remarks=remarks,
        )

        db.add(history)

    @staticmethod
    def update_status(
        db: Session,
        order_id: int,
        user_id: int,
        new_status: str,
        remarks: str = None,
    ):

        order = (
            db.query(Order)
            .filter(Order.id == order_id)
            .first()
        )

        if order is None:
            raise Exception("Order not found")

        # Update order status
        order.status = new_status

        # Add tracking history
        TrackingService.add_tracking(
            db=db,
            order_id=order.id,
            status=new_status,
            updated_by=user_id,
            remarks=remarks,
        )

        # If delivered, free the agent
        if (
            new_status == OrderStatus.DELIVERED
            and order.agent_id is not None
        ):

            agent = (
                db.query(Agent)
                .filter(Agent.id == order.agent_id)
                .first()
            )

            if agent:
                agent.status = AgentStatus.AVAILABLE

        db.commit()
        db.refresh(order)

        return order

    @staticmethod
    def get_tracking_history(
        db: Session,
        order_id: int,
    ):

        return (
            db.query(TrackingHistory)
            .filter(
                TrackingHistory.order_id == order_id
            )
            .order_by(
                TrackingHistory.timestamp.asc()
            )
            .all()
        )