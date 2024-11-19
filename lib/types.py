from pydantic import BaseModel, validator


class User(BaseModel):
    email: str
    username: str

    @validator("email")
    def validate_email(cls, v):
        if len(v) <= 0:
            raise ValueError("Email is a required field")
        elif "@" not in v or "." not in v:
            raise ValueError("Invalid Email value")
        return v
