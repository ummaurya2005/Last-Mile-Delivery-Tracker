from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TrackingUpdate(BaseModel):
    remarks: str | None = None


class TrackingResponse(BaseModel):
    id: int
    order_id: int
    status: str
    updated_by: int
    timestamp: datetime
    remarks: str | None = None

    model_config = ConfigDict(from_attributes=True)