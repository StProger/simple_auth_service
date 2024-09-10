from fastapi import APIRouter, Depends

from asyncpg.pool import Pool

from app.repository.base import BaseRepository
from app.repository.users.repository import UsersRepository

from app.db import Database

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/login")
async def login(pool: Pool = Depends(Database.get_pool)):

    result = await UsersRepository.find_one_or_none("ewgwebw", pool)
    return result
