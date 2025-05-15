from fastapi import FastAPI
from app.config import settings
from app.routers import calculator

app = FastAPI(title=settings.app_name, debug=settings.debug)

app.include_router(calculator.router)
