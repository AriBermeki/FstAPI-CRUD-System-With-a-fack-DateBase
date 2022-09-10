import uuid
from typing import List, Any

from fastapi.routing import APIRouter
from fastapi import Depends, HTTPException, status

from Database.Schema.schema import AccountSchema
from Database.database import database

# from Database.Models.models import Accounts

create_router = APIRouter()




@create_router.post('/new_user', response_model=AccountSchema, status_code=status.HTTP_201_CREATED)
async def create(accounts: AccountSchema):

#____________ Hier wird die Daten nach eine bestimmte Schema in der Daten Bank geschpiechert______________#

    new_user = accounts.dict()
    new_user['id'] = uuid.uuid4()
    new_user['email'] = new_user['email']
    new_user['username'] = new_user['username']
    new_user['password'] = new_user['password']
    new_user['confirm_password'] = new_user['confirm_password']
    new_user['date_joiend'] = new_user['date_joiend']
    new_user['role'] = new_user['role']
    new_user['priority'] = new_user['priority']
    new_user['status'] = new_user['status']
    database.append(new_user)
    return new_user
