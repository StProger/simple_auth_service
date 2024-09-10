from datetime import datetime, timedelta

from jose import jwt
from asyncpg import Pool
from passlib.context import CryptContext
from pydantic import EmailStr
import pytz

from app.models.user import User
from app.settings import settings
from app.repository.users.repository import UsersRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:

    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:

    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:

    to_encode = data.copy()
    expire = datetime.now(pytz.timezone("Europe/Moscow")) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, settings.ALGORITHM
    )
    return encode_jwt


async def authenticate_user(login: str, password: str, pool: Pool) -> None | User:

    user = await UsersRepository.find_one_or_none(login=login, pool=pool)

    if user:
        user = User(**user)

    if not user or not verify_password(password, user.hashed_password):
        return None

    else:
        return user
