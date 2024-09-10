from pydantic import BaseModel


class User(BaseModel):

    id: int
    login: str
    hashed_password: str