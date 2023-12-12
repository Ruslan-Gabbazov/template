from fastapi import APIRouter

from api.v1.item import router as item_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(item_router)

api_router = APIRouter(prefix="/api")
api_router.include_router(v1_router)
