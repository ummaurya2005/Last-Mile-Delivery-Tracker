from pydantic import BaseModel


class AgentCreate(BaseModel):
    user_id: int
    zone: str


class AgentResponse(BaseModel):
    id: int
    user_id: int
    zone: str
    status: str

    class Config:
        from_attributes = True