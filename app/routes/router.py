from fastapi import APIRouter, Depends

from asyncpg.connection import Connection

from app.db import Database

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/login")
async def login(connection: Connection = Depends(Database.get_pool)):

    print(connection)
