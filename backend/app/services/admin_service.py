from sqlalchemy.orm import Session

from app.models.zone import Zone
from app.schemas.zone import ZoneCreate
from app.models.rate_card import RateCard
from app.schemas.rate_card import RateCardCreate


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