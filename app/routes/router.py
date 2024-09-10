from fastapi import APIRouter, Depends, Response

from asyncpg.pool import Pool

from app.auth import authenticate_user, create_access_token, get_password_hash
from app.exceptions.auth_exceptions import IncorrectLoginOrPasswordException, UserAlreadyExistsException
from app.repository.users.repository import UsersRepository

from app.db import Database
from app.schemas import SUserLogin, SUserRegistration

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/login")
async def login(user_data: SUserLogin,
                response: Response,
                pool: Pool = Depends(Database.get_pool),
                ):
    user = await authenticate_user(login=user_data.login, password=user_data.password, pool=pool)

    if not user:
        raise IncorrectLoginOrPasswordException

    access_token = create_access_token(
        {"sub": str(user.id)}
    )
    response.set_cookie("access_token", access_token, httponly=True, max_age=86400)
    return {"access_token": access_token}


@router.post("/register")
async def register_user(user_data: SUserRegistration,
                        pool: Pool = Depends(Database.get_pool)):
    existing_user = await UsersRepository.find_one_or_none(login=user_data.login, pool=pool)

    if existing_user:
        raise UserAlreadyExistsException

    hashed_password = get_password_hash(user_data.password)
    await UsersRepository.add(login=user_data.login, hashed_password=hashed_password, pool=pool)

    return {"message": "user registered successfully"}



