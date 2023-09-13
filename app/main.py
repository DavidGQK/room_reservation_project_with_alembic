from fastapi import FastAPI

from app.api.routers import main_router
from app.core.config import settings
# import coroutine for creating superuser
from app.core.init_db import create_first_superuser

app = FastAPI(title=settings.app_title)

app.include_router(main_router)

# start coroutine create_first_superuser.
@app.on_event('startup')
async def startup():
    await create_first_superuser() 