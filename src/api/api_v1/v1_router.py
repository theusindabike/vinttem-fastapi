from fastapi import APIRouter

from src.api.api_v1 import transactions

router = APIRouter()
router.include_router(
    transactions.router, tags=["transactions"], prefix="/transactions"
)
