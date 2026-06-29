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


class TrackingHistory(Base):
    __tablename__ = "tracking_history"

    id = Column(Integer, primary_key=True, index=True)

    order_id = Column(Integer, ForeignKey("orders.id"))

    status = Column(String, nullable=False)

    updated_by = Column(Integer, ForeignKey("users.id"))

    timestamp = Column(DateTime, default=datetime.utcnow)

    remarks = Column(String, nullable=True)

    order = relationship("Order")

    user = relationship("User")