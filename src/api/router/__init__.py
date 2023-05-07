from fastapi import APIRouter

from src.api.router import chat_endpoint

api_router = APIRouter()

api_router.include_router(chat_endpoint.router, prefix="/chat", tags=["CHAT"])