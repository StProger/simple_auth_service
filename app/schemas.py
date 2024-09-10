from pydantic import BaseModel


class SUserLogin(BaseModel):

    login: str
    password: str


class SUserRegistration(BaseModel):

    login: str
    password: str