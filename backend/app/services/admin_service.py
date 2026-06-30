from sqlalchemy.orm import Session
from app.utils.constants import AgentStatus
from app.models.zone import Zone
from app.schemas.zone import ZoneCreate
from app.models.rate_card import RateCard
from app.schemas.rate_card import RateCardCreate
from app.models.agent import Agent
from app.models.user import User
from app.schemas.agent import AgentCreate


class AdminService:

    @staticmethod
    def create_zone(
        db: Session,
        zone: ZoneCreate
    ):

        existing = (
            db.query(Zone)
            .filter(Zone.zone_name == zone.zone_name)
            .first()
        )

        if existing:
            raise Exception("Zone already exists")

        db_zone = Zone(
            zone_name=zone.zone_name,
            city=zone.city,
            state=zone.state,
        )

        db.add(db_zone)
        db.commit()
        db.refresh(db_zone)

        return db_zone

    @staticmethod
    def get_all_zones(db: Session):

        return db.query(Zone).all()

    @staticmethod
    def create_rate_card(
        db: Session,
        rate: RateCardCreate,
        ):

        db_rate = RateCard(
        pickup_zone_id=rate.pickup_zone_id,
        drop_zone_id=rate.drop_zone_id,
        order_type=rate.order_type,
        rate_per_kg=rate.rate_per_kg,
        cod_charge=rate.cod_charge,
         )

        db.add(db_rate)
        db.commit()
        db.refresh(db_rate)

        return db_rate


    @staticmethod
    def get_all_rate_cards(db: Session):

        return db.query(RateCard).all()
    

    @staticmethod
    def create_agent(
        db: Session,
        agent: AgentCreate,
    ):

        user = (
            db.query(User)
            .filter(User.email == agent.email)
            .first()
        )

        if user is None:
            raise Exception("Agent user not found")

        if user.role.lower() != "agent":
            raise Exception("User is not registered as an agent")

        existing = (
            db.query(Agent)
            .filter(Agent.user_id == user.id)
            .first()
        )

        if existing:
            raise Exception("Agent profile already exists")

        db_agent = Agent(
            user_id=user.id,
            assigned_zone_id=agent.assigned_zone_id,
            vehicle_type=agent.vehicle_type,
            status=AgentStatus.AVAILABLE
        )

        db.add(db_agent)
        db.commit()
        db.refresh(db_agent)

        return db_agent


    @staticmethod
    def get_all_agents(db: Session):

        return db.query(Agent).all()