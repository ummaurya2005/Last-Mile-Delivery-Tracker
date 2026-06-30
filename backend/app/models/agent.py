from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    assigned_zone_id = Column(
        Integer,
        ForeignKey("zones.id"),
        nullable=False
    )

    vehicle_type = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        default="AVAILABLE"
    )

    user = relationship("User")

    assigned_zone = relationship("Zone")