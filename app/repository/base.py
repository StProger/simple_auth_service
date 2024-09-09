from asyncpg.connection import Connection


class BaseRepository:

    @classmethod
    async def find_by_id(cls, model_name: str, model_id: int, connection: Connection):

        query = f"""SELECT * FROM {model_name} WHERE id = $model_id"""

        stmt = await connection.prepare(query)

        return await stmt.fetchrow(model_id)
