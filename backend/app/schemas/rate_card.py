from pydantic import BaseModel, ConfigDict


class RateCardCreate(BaseModel):
    pickup_zone_id: int
    drop_zone_id: int
    order_type: str
    rate_per_kg: float
    cod_charge: float


class RateCardUpdate(BaseModel):
    pickup_zone_id: int
    drop_zone_id: int
    order_type: str
    rate_per_kg: float
    cod_charge: float


class RateCardResponse(BaseModel):
    id: int
    pickup_zone_id: int
    drop_zone_id: int
    order_type: str
    rate_per_kg: float
    cod_charge: float

    model_config = ConfigDict(from_attributes=True)