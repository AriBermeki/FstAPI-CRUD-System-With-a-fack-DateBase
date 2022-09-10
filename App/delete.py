import uuid

from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRoute, APIRouter
from fastapi.requests import Request
from fastapi.responses import Response
from Database.Schema.schema import AccountSchema
from Database.Schema.schema import AccountSchema
from Database.database import database

delete_router = APIRouter()


@delete_router.delete('/delete_user/{user_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response,)
async def delete(user_id: uuid.UUID):

#____________ Hier wird untersucht, ob die Output ID gleich der Input ID ist, wenn ja, dann wird die daten aus der Daten Bank gelöscht, wenn nicht wird eine Fehle zurück gegeben , dass diese eingegebene ID nicht exestiert ist______________#


    for x,item in enumerate(database):
        if item['id'] == user_id:
            database.pop(x)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'User with ID: {user_id} not found'
    )
