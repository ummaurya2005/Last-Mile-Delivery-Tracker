from sqlalchemy import Column, Integer, String

from app.database import Base


class Zone(Base):
    __tablename__ = "zones"

    id = Column(Integer, primary_key=True, index=True)

    zone_name = Column(String, unique=True, nullable=False)

    city = Column(String, nullable=False)

    state = Column(String, nullable=False)