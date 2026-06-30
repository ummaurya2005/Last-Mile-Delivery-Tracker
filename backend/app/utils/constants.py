"""
Application Constants

This file contains all constant values used across the project.
Avoid hardcoding roles, statuses, order types, and payment types.
"""


class UserRole:
    ADMIN = "admin"
    CUSTOMER = "customer"
    AGENT = "agent"


class AgentStatus:
    AVAILABLE = "AVAILABLE"
    BUSY = "BUSY"
    OFFLINE = "OFFLINE"


class OrderStatus:
    CREATED = "CREATED"
    ASSIGNED = "ASSIGNED"
    PICKED_UP = "PICKED_UP"
    IN_TRANSIT = "IN_TRANSIT"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"
    PENDING_ASSIGNMENT = "PENDING_ASSIGNMENT"


class OrderType:
    B2B = "B2B"
    B2C = "B2C"


class PaymentType:
    PREPAID = "PREPAID"
    COD = "COD"


class VehicleType:
    BIKE = "Bike"
    CYCLE = "Cycle"
    VAN = "Van"