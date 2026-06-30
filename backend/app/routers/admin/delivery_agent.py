from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_admin

from app.schemas.agent import (
    AgentCreate,
    AgentResponse,
)

from app.services.admin_service import AdminService

router = APIRouter(
    prefix="/admin/agents",
    tags=["Admin - Agents"]
)


@router.post(
    "",
    response_model=AgentResponse,
    status_code=201
)
def create_agent(
    agent: AgentCreate,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin),
):

    try:

        return AdminService.create_agent(
            db,
            agent,
        )

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get(
    "",
    response_model=list[AgentResponse],
)
def get_agents(
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin),
):

    return AdminService.get_all_agents(db)