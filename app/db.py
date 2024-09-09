import asyncpg

from app.settings import settings


class Database:

    _instance_pool = None

    @classmethod
    async def get_pool(cls):
        if cls._instance_pool is None:
            cls._instance_pool = await asyncpg.connect(
                host=settings.DB_HOST,
                port=settings.DB_PORT,
                user=settings.DB_USER,
                password=settings.DB_PASSWORD,
                database=settings.DB_NAME
            )
        return cls._instance_pool

    @classmethod
    async def close_pool(cls):
        if cls._instance_pool:
            await cls._instance_pool.close()
            cls._instance_pool = None
