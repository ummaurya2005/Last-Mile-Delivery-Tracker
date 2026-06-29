from pydantic import BaseModel, ConfigDict


class ZoneCreate(BaseModel):
    zone_name: str
    city: str
    state: str


class ZoneUpdate(BaseModel):
    zone_name: str
    city: str
    state: str


class ZoneResponse(BaseModel):
    id: int
    zone_name: str
    city: str
    state: str

    model_config = ConfigDict(from_attributes=True)