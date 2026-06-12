from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.views.http_types.http_request import HttpRequest
from src.main.composer.user_finder_composer import user_finder_composer



users_routes = APIRouter(tags=["usuários"])

@users_routes.post("/users")
async def criar_usuario():

    return JSONResponse(content={"message": "Usuário criado com sucesso!"},
                         status_code=201)

@users_routes.get("/users/{username}")
async def buscar_usuarios_por_nome(username: str):
    http_request = HttpRequest(path_params={"username": username})
    user_finder = user_finder_composer()

    http_response = await user_finder.handle_find_user(http_request)
    
    return JSONResponse(content=http_response.body,
                        status_code=http_response.status_code)