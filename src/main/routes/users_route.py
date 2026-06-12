from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.views.http_types.http_request import HttpRequest
from src.validators.user_register_validator import UserInput

from src.main.composer.user_finder_composer import user_finder_composer
from src.main.composer.user_register_composer import user_register_composer

users_routes = APIRouter(tags=["usuários"])

@users_routes.post("/users")
async def criar_usuario(body: UserInput):
    http_request = HttpRequest(body=dict(body))
    user_register = user_register_composer()

    http_response = await user_register.handle_register_user(http_request)
    
    return JSONResponse(content=http_response.body,
                         status_code=http_response.status_code)

@users_routes.get("/users/{username}")
async def buscar_usuarios_por_nome(username: str):
    http_request = HttpRequest(path_params={"username": username})
    user_finder = user_finder_composer()

    http_response = await user_finder.handle_find_user(http_request)
    
    return JSONResponse(content=http_response.body,
                        status_code=http_response.status_code)