from fastapi import APIRouter
from .endpoints import auth, data, ml, websocket

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(auth.router)
api_router.include_router(data.router)
api_router.include_router(ml.router)
api_router.include_router(websocket.router)
