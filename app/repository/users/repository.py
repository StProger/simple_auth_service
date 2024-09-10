from asyncpg.pool import Pool
from asyncpg import Record

from app.repository.base import BaseRepository


class UsersRepository(BaseRepository):

    model = "users"

    @classmethod
    async def find_one_or_none(cls, login: str, pool: Pool):

        async with pool.acquire() as connection:
            async with connection.transaction():

                query = f"""SELECT * FROM {cls.model} WHERE login = $1"""

                result: Record = await connection.fetchrow(query, login)
                print(dict(result))

