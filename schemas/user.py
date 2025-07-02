from pydantic import BaseModel, EmailStr
from typing import List, Optional
from enum import Enum


class EmailType(str, Enum):
    activation = "activation"
    confirmation = "confirmation"
    password_reset = "password_reset"
    newsletter = "newsletter"


class EmailBase(BaseModel):
    to_email: EmailStr
    from_email: EmailStr
    from_password: str
    html_content: str
    type: EmailType
    
    class Config:
        from_attributes = True

class EmailCreate(EmailBase):
    pass

