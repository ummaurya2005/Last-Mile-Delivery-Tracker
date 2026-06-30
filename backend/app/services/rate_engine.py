from sqlalchemy.orm import Session

from app.models.rate_card import RateCard


class RateEngine:

    @staticmethod
    def calculate_volumetric_weight(
        length: float,
        breadth: float,
        height: float,
    ) -> float:

        return (length * breadth * height) / 5000

    @staticmethod
    def calculate_chargeable_weight(
        actual_weight: float,
        volumetric_weight: float,
    ) -> float:

        return max(actual_weight, volumetric_weight)

    @staticmethod
    def calculate_delivery_charge(
        db: Session,
        pickup_zone_id: int,
        drop_zone_id: int,
        order_type: str,
        payment_type: str,
        chargeable_weight: float,
    ):

        rate = (
            db.query(RateCard)
            .filter(
                RateCard.pickup_zone_id == pickup_zone_id,
                RateCard.drop_zone_id == drop_zone_id,
                RateCard.order_type == order_type,
            )
            .first()
        )

        if rate is None:
            raise Exception("Rate Card not found")

        delivery_charge = (
            chargeable_weight * rate.rate_per_kg
        )

        if payment_type.upper() == "COD":
            delivery_charge += rate.cod_charge

        return delivery_charge