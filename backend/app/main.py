from fastapi import FastAPI

from app.routers import auth
from app.database import Base, engine

# Import all models so SQLAlchemy registers them
import app.models
from app.routers.admin import zone_router
from app.routers.admin import (
    zone_router,
    rate_card_router,
)

# Create database tables
Base.metadata.create_all(bind=engine)



app = FastAPI(
    title="Last Mile Delivery Tracker",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(zone_router)
app.include_router(rate_card_router)
@app.get("/")
def home():
    return {
        "message": "Backend Running Successfully"
    }