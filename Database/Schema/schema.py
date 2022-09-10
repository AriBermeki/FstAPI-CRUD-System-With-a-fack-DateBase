from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel, EmailStr
from enum import Enum
from datetime import datetime




class Priority(Enum):
    high = 'high'
    medium = 'medium'
    low = 'low'


class Status(Enum):
    completed = 'completed'
    progress = 'progress'
    pending = 'pending'


class Role(Enum):
    is_admin= 'is_admin'
    is_active = 'is_active'
    is_staff = 'is_staff'
    is_superuser = 'is_superuser'



class AccountSchema(BaseModel):
    id: Optional[UUID] = None
    email: EmailStr
    username: str
    password: str
    confirm_password: str
    date_joiend: datetime
    priority: Optional[Priority]  = None
    status: Optional[Status]  = None
    role: Optional[Role] = None

    class Config:
        orm_mode = True


class NewAccountSchema(BaseModel):
    id: Optional[UUID] = None
    email: EmailStr
    username: str
    password: str
    confirm_password: str
    date_joiend: datetime
    priority: Optional[Priority]  = None
    status: Optional[Status]  = None
    role: Optional[Role] = None

    class Config:
        orm_mode = True





class ProfileSchema(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    birth_data: Optional[datetime] = None
    address: Optional[str] = None
    apartment_number: Optional[int] = None
    zip: Optional[int] = None
    city: Optional[str] = None
    profile_pictor: Optional[str] = None
    avatar: Optional[str] = None
    bio: Optional[str] = None

    class Config:
        orm_mode = True





