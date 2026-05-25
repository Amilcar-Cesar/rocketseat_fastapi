from fastapi import FastAPI
from src.main.routes.users_route import users_routes



app = FastAPI()
app.include_router(users_routes)