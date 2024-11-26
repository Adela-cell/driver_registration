# app/models.py
from pydantic import BaseModel
from typing import Optional

class Driver(BaseModel):
    name: str
    phone: str
    email: Optional[str]
    license_number: str
    address: Optional[str]
