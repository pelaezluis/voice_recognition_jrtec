from fastapi import APIRouter
from .endpoints import recognition

api_router = APIRouter()

api_router.include_router(recognition.router, prefix='/recognition', tags=['Voice recognition'])