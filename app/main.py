from fastapi import FastAPI
from app.routers.home import router as home_router
from app.database.database import Base, engine
from app.models.user import User
from app.routers.user import router as user_router

app = FastAPI(
    title="LegacyAI API",
    description="Institutional Intelligence Platform",
    version="1.0.0"
)

app.include_router(home_router)
Base.metadata.create_all(bind=engine)
app.include_router(user_router)