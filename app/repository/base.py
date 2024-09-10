from asyncpg.connection import Connection
from asyncpg.pool import Pool


class BaseRepository:

    model = None

    @classmethod
    async def find_by_id(cls, model_name: str, model_id: int, pool: Pool):

        async with pool.acquire() as connection:
            async with connection.transaction():

                query = f"""SELECT * FROM {cls.model} WHERE id = $1"""

                return await connection.fetchrow(query, model_id)
