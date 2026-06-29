from fastapi import FastAPI
from app.database import Base, engine

from app.models.user import User
from app.models.agent import Agent
from app.models.zone import Zone
from app.models.rate_card import RateCard
from app.models.order import Order
from app.models.tracking import TrackingHistory
from app.models.notification import Notification


app = FastAPI(
    title="Last Mile Delivery Tracker",
    version="1.0"
)


@app.get("/")
def home():

    return {
        "message": "Backend Running Successfully"
    }

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Last Mile Delivery Tracker"
)


@app.get("/")
def home():
    return {
        "message": "Backend Running Successfully"
    }