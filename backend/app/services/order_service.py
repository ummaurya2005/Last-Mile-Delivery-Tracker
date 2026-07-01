from sqlalchemy.orm import Session

from app.models.order import Order
from app.models.user import User

from app.schemas.order import OrderCreate

from app.services.rate_engine import RateEngine
from app.services.assignment_service import AssignmentService
from app.services.tracking_service import TrackingService

from app.utils.constants import OrderStatus


class OrderService:

    @staticmethod
    def create_order(
        db: Session,
        customer: User,
        order: OrderCreate,
    ):

        # Calculate volumetric weight
        volumetric_weight = (
            RateEngine.calculate_volumetric_weight(
                order.length,
                order.breadth,
                order.height,
            )
        )

        # Calculate chargeable weight
        chargeable_weight = (
            RateEngine.calculate_chargeable_weight(
                order.actual_weight,
                volumetric_weight,
            )
        )

        # Calculate delivery charge
        delivery_charge = (
            RateEngine.calculate_delivery_charge(
                db=db,
                pickup_zone_id=order.pickup_zone_id,
                drop_zone_id=order.drop_zone_id,
                order_type=order.order_type,
                payment_type=order.payment_type,
                chargeable_weight=chargeable_weight,
            )
        )

        # Create Order
        db_order = Order(
            customer_id=customer.id,

            pickup_zone_id=order.pickup_zone_id,
            drop_zone_id=order.drop_zone_id,

            pickup_address=order.pickup_address,
            drop_address=order.drop_address,

            length=order.length,
            breadth=order.breadth,
            height=order.height,

            actual_weight=order.actual_weight,

            volumetric_weight=volumetric_weight,
            chargeable_weight=chargeable_weight,

            order_type=order.order_type,
            payment_type=order.payment_type,

            delivery_charge=delivery_charge,

            status=OrderStatus.CREATED,
        )

        # Save order
        db.add(db_order)
        db.commit()
        db.refresh(db_order)

        # Add tracking entry
        TrackingService.add_tracking(
            db=db,
            order_id=db_order.id,
            status=OrderStatus.CREATED,
            updated_by=customer.id,
            remarks="Order Created",
        )

        db.commit()

        # Automatically assign an agent
        db_order = AssignmentService.assign_agent(
            db=db,
            order=db_order,
        )

        return db_order

    @staticmethod
    def get_customer_orders(
        db: Session,
        customer: User,
    ):

        return (
            db.query(Order)
            .filter(
                Order.customer_id == customer.id
            )
            .all()
        )