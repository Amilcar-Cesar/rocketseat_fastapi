from fastapi import APIRouter
from fastapi.responses import JSONResponse

users_routes = APIRouter(tags=["usuários"])

@users_routes.post("/users")
async def criar_usuario():

    return JSONResponse(content={"message": "Usuário criado com sucesso!"},
                         status_code=201)