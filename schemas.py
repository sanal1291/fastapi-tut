from typing import Optional
from pydantic import BaseModel
from passlib.context import CryptContext

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$0UbL7MSHvSmL3FpOsciOBODINSgNKxzC289iSlC3sd6nz2c/XhtuO",
        "disabled": False,
    }
}


class CustomUser(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class UserInDB(CustomUser):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "e44f4c169be90385a93b8850b974e03f16a41b6f789062630edf435ba5aeb134"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
