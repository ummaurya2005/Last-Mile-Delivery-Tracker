from pydantic import BaseModel, ConfigDict


class AgentCreate(BaseModel):
    email: str
    assigned_zone_id: int
    vehicle_type: str


class AgentUpdate(BaseModel):
    assigned_zone_id: int
    vehicle_type: str
    status: str


class AgentResponse(BaseModel):
    id: int
    user_id: int
    assigned_zone_id: int
    vehicle_type: str
    status: str

    model_config = ConfigDict(from_attributes=True)