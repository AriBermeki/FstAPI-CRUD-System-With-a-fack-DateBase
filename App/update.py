import uuid

from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRoute, APIRouter
from fastapi.requests import Request
from fastapi.responses import Response
from Database.Schema.schema import AccountSchema, NewAccountSchema
from App.create import user
update_router = APIRouter()


@update_router.post('/update_user/{user_id}', status_code=status.HTTP_202_ACCEPTED, response_model= NewAccountSchema)   
async def update(user_id: uuid.UUID, data: AccountSchema): 
#____________ Hier wird untersucht, ob die Output Daten gleich der Input is ______________#
    for item in user:
        if item['id'] == user_id:
            if data.id is not None:
                data.id = data.id
            if data.email is not None:
                data.email = data.email
            if data.username is not None:
                data.username = data.username
            if data.password is not None:
                data.password = data.password
            if data.confirm_password is not None:
                data.confirm_password = data.confirm_password
            if data.date_joiend is not None:
                data.date_joiend = data.date_joiend
            if data.priority is not None:
                data.priority = data.priority
            if data.status is not None:
                data.status = data.status
            if data.role is not None:
                data.role = data.role
            item.update(data.dict())
            return item
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'User with ID: {user_id} not found'
    )


