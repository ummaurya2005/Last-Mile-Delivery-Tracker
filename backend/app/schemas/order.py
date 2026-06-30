from pydantic import BaseModel, ConfigDict


class OrderCreate(BaseModel):
    pickup_zone_id: int
    drop_zone_id: int

    pickup_address: str
    drop_address: str

    length: float
    breadth: float
    height: float

    actual_weight: float

    order_type: str
    payment_type: str


class OrderResponse(BaseModel):
    id: int

    customer_id: int

    pickup_zone_id: int
    drop_zone_id: int

    pickup_address: str
    drop_address: str

    length: float
    breadth: float
    height: float

    actual_weight: float
    volumetric_weight: float
    chargeable_weight: float

    order_type: str
    payment_type: str

    delivery_charge: float

    status: str

    model_config = ConfigDict(from_attributes=True)