from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

import structlog
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.endpoints.system import router as router_system

from system.settings import Settings

# Create logger
logger = structlog.get_logger()


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI) -> AsyncIterator:
    logger.info("Startup finished", env=Settings().ENVIRONMENT.value)
    yield
    await logger.ainfo("Application is shutting down")


# Set up FastApi
fastapi_app = FastAPI(lifespan=lifespan, title="Caro API")
fastapi_app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=[Settings().FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
fastapi_app.include_router(router_system)
