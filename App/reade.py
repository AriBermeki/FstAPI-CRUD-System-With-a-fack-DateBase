from typing import List, Union
import uuid

from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRoute, APIRouter
from fastapi.requests import Request
from fastapi.responses import Response
from Database.Schema.schema import AccountSchema
from App.create import user

reade_router = APIRouter()


@reade_router.get('/reade_user', response_model=List[AccountSchema])
#____________ Hier wird alle daten in der Daten Bank  zurück gegeben ______________#
async def reade():
    
    return user
    


@reade_router.get('/reade_use/{user_id}', response_model=AccountSchema)
async def reade(user_id: uuid.UUID):

#____________ Hier wird untersucht, ob die Output ID gleich der Input ID ist, wenn ja, dann wird die daten gezeigt, wenn nicht wird eine Fehle zurück gegeben ______________#

    for item in user:
        if item['id'] == user_id:
            return item
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'User with ID: {user_id} not found'
    )
