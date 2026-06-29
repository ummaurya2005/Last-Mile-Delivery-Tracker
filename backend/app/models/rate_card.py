from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class RateCard(Base):
    __tablename__ = "rate_cards"

    id = Column(Integer, primary_key=True, index=True)

    pickup_zone_id = Column(Integer, ForeignKey("zones.id"))

    drop_zone_id = Column(Integer, ForeignKey("zones.id"))

    order_type = Column(String, nullable=False)
    # B2B / B2C

    rate_per_kg = Column(Float, nullable=False)

    cod_charge = Column(Float, default=0)

    pickup_zone = relationship(
        "Zone",
        foreign_keys=[pickup_zone_id]
    )

    drop_zone = relationship(
        "Zone",
        foreign_keys=[drop_zone_id]
    )