from fastapi import FastAPI
from src.api import main_router


def start_application() -> FastAPI:
    application = FastAPI()
    application.include_router(main_router.router, prefix="/api")

    return application


app = start_application()
