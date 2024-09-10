from fastapi import HTTPException, status


class AuthException(HTTPException):

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = 'An unexpected error has occurred.'

    def __init__(self):

        super().__init__(status_code=self.status_code, detail=self.detail)


class IncorrectLoginOrPasswordException(AuthException):

    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect login or password."


class UserAlreadyExistsException(AuthException):

    status_code = status.HTTP_409_CONFLICT
    detail = "User already exists."
