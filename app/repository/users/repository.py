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
                if result:
                    return dict(result)
                return result

    @classmethod
    async def add(cls, login: str, hashed_password: str, pool: Pool):

        async with pool.acquire() as connection:
            async with connection.transaction():

                query = f"""INSERT INTO {cls.model} (login, hashed_password) VALUES ($1, $2)"""

                await connection.execute(query, login, hashed_password)
