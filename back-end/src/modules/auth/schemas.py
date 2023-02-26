from pydantic import BaseModel, EmailStr, constr, validator
from datetime import datetime
import re

class UserCredentials(BaseModel):
    email: EmailStr
    password: constr(
        min_length=8,
        max_length=64
    )

    @validator('password')
    def password_must_be_strong(cls, v):
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+-=]).*$", v): 
            raise ValueError('password must contain at least one uppercase letter, one lowercase letter, one number, and one special character')
        return v


class UserCreate(UserCredentials):
    name: constr(min_length=4, max_length=16)


class User(BaseModel):
    id: int
    name: str
    email: str
    is_admin: bool = False
    is_active: bool = True
    email_verified: bool = False

    last_login: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
