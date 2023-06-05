from fastapi import FastAPI, APIRouter

from src.transactions import router as transactions
from src.db import create_db_and_tables, engine


def start_application() -> FastAPI:
    application = FastAPI(title="Vinttem API")

    router = APIRouter()
    router.include_router(
        transactions.router, tags=["transactions"], prefix="/v1/transactions"
    )
    application.include_router(router, prefix="/api")

    return application


app = start_application()


@app.on_event("startup")
def on_startup():
    create_db_and_tables(engine)
