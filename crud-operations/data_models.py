from pydantic import BaseModel
from typing import Optional


class NewEmployee(BaseModel):
    name: str
    age: int
    pos: str


class UpdateEmployee(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    pos: Optional[str] = None