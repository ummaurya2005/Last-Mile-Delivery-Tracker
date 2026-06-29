from pydantic import BaseModel


class ZoneCreate(BaseModel):
    zone_name: str
    city: str
    state: str


class ZoneResponse(ZoneCreate):
    id: int

    class Config:
        from_attributes = True