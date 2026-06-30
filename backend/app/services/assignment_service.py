from sqlalchemy.orm import Session

from app.models.agent import Agent
from app.models.order import Order


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
                Agent.status == "AVAILABLE",
            )
            .first()
        )

        if agent is None:

            order.status = "Pending Assignment"

            db.commit()

            db.refresh(order)

            return order

        order.agent_id = agent.id

        order.status = "ASSIGNED"

        agent.status = "BUSY"

        db.commit()

        db.refresh(order)

        return order