from pydantic import BaseModel, EmailStr


class Person(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
