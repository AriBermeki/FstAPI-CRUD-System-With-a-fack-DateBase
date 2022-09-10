from fastapi.routing import APIRoute
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from App.create import create_router
from App.delete import delete_router
from App.reade import reade_router
from App.update import update_router


app = FastAPI(
    title="GoQuanto is a Scientific  Platform",
    description="Mathematics  Physics  Chemistry",
    version="0.0.1",
    contact={
        "Organisation Name":"GoQuanto is a Scientific  Platform",
        "CTO Email": 'ari.bermeki@icloud.com',
        "Organisation Address":"Germany, Berlin"
    },
    license_info={
        "name":"MIT"
    }
)
app.include_router(reade_router)
app.include_router(create_router)
app.include_router(update_router)
app.include_router(delete_router)