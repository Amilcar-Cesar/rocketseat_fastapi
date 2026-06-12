import pytest
from .user_register_view import UserRegisterView
from .http_types.http_request import HttpRequest

class MockUserRegister:
    def __init__(self):
        self.register_user_att = {}

    async def register_user(self, user_data: dict) -> dict:
        self.register_user_att = user_data
        return {
            "type": "users",
            "count": 1,
            "message": "Usuário registrado com sucesso.",
            "attributes": user_data,
        }
    
class MockUserRegisterError:
    async def register_user(self, user_data: dict) -> dict:
        raise Exception("Erro ao registrar usuário.")
    
@pytest.mark.asyncio
async def test_register_user_view():
    controller = MockUserRegister()
    view = UserRegisterView(controller)

    user_data = {
        "username": "João",
        "age": 25,
        "uf": "SP",
    }

    http_request = HttpRequest(body=user_data)
    response = await view.handle_register_user(http_request)

    assert controller.register_user_att == user_data
    assert response.status_code == 201
    assert response.body["type"] == "users"
    assert response.body["count"] == 1
    assert response.body["attributes"] == user_data

@pytest.mark.asyncio
async def test_register_user_view_error():
    controller = MockUserRegisterError()
    view = UserRegisterView(controller)

    user_data = {
        "username": "João",
        "age": 25,
        "uf": "SP",
    }

    http_request = HttpRequest(body=user_data)
    response = await view.handle_register_user(http_request)

    assert response.status_code == 400
    assert "error" in response.body
    assert response.body["error"] == "Erro ao registrar usuário."