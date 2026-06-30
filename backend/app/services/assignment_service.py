from sqlalchemy.orm import Session

from app.models.agent import Agent
from app.models.order import Order
from app.utils.constants import (
    AgentStatus,
    OrderStatus,
)

class AssignmentService:

    @staticmethod
    def assign_agent(
        db: Session,
        order: Order,
    ):

        agent = (
            db.query(Agent)
            .filter(
                Agent.assigned_zone_id == order.pickup_zone_id,
                Agent.status == AgentStatus.AVAILABLE,
            )
            .first()
        )

        if agent is None:

            order.status = OrderStatus.PENDING_ASSIGNMENT

            db.commit()

            db.refresh(order)

            return order

        order.agent_id = agent.id

        order.status = OrderStatus.ASSIGNED,

        agent.status = AgentStatus.BUSY

        db.commit()

        db.refresh(order)

        return order