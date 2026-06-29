from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    order_id = Column(Integer, ForeignKey("orders.id"))

    notification_type = Column(String)
    # Email / SMS

    message = Column(String)

    status = Column(String, default="Sent")

    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")

    order = relationship("Order")