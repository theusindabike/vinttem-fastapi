from fastapi import APIRouter

from src.api.api_v1 import v1_router

router = APIRouter()

router.include_router(v1_router.router, prefix="/v1")
