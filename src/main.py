from fastapi import FastAPI

from src.api import main_router
from src.db import create_db_and_tables, engine


def start_application() -> FastAPI:
    application = FastAPI(title="Vinttem API")
    application.include_router(main_router.router, prefix="/api")

    return application


app = start_application()


@app.on_event("startup")
def on_startup():
    create_db_and_tables(engine)
