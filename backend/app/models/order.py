from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    customer_id = Column(Integer, ForeignKey("users.id"))

    agent_id = Column(Integer, ForeignKey("agents.id"), nullable=True)

    pickup_zone_id = Column(Integer, ForeignKey("zones.id"))

    drop_zone_id = Column(Integer, ForeignKey("zones.id"))

    pickup_address = Column(String, nullable=False)

    drop_address = Column(String, nullable=False)

    length = Column(Float)

    breadth = Column(Float)

    height = Column(Float)

    actual_weight = Column(Float)

    volumetric_weight = Column(Float)

    chargeable_weight = Column(Float)

    order_type = Column(String)
    # B2B / B2C

    payment_type = Column(String)
    # Prepaid / COD

    delivery_charge = Column(Float)

    status = Column(String, default="Created")

    customer = relationship("User")

    agent = relationship("Agent")

    pickup_zone = relationship(
        "Zone",
        foreign_keys=[pickup_zone_id]
    )

    drop_zone = relationship(
        "Zone",
        foreign_keys=[drop_zone_id]
    )