from fastapi import FastAPI

from contextlib import asynccontextmanager

from app.routes.router import router as auth_router
from app.db import Database


@asynccontextmanager
async def lifespan(_: FastAPI):

    await Database.get_pool()
    yield
    await Database.close_pool()

app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)
