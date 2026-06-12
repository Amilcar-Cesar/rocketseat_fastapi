import pytest

from .http_types.http_request import HttpRequest
from .user_update_view import UserUpdateView


class MockUserUpdate:
    def __init__(self):
        self.update_user_att = {}

    async def update_user(self, user_id: int, updated_infos: dict) -> dict:
        self.update_user_att = {
            "user_id": user_id,
            "updated_infos": updated_infos,
        }
        return {
            "type": "users",
            "count": 1,
            "message": "Usuário atualizado com sucesso.",
            "attributes": updated_infos,
        }


class MockUserUpdateError:
    async def update_user(self, user_id: int, updated_infos: dict) -> dict:
        raise Exception("Usuário não encontrado.")


@pytest.mark.asyncio
async def test_update_user_view():
    controller = MockUserUpdate()
    view = UserUpdateView(controller)

    user_id = 1
    updated_infos = {
        "username": "Ana",
        "age": 20,
        "uf": "MG",
    }

    http_request = HttpRequest(
        body=updated_infos,
        path_params={"user_id": user_id},
    )

    response = await view.handle_update_user(http_request)

    assert controller.update_user_att["user_id"] == user_id
    assert controller.update_user_att["updated_infos"] == updated_infos

    assert response.status_code == 200
    assert response.body["type"] == "users"
    assert response.body["count"] == 1
    assert response.body["attributes"] == updated_infos


@pytest.mark.asyncio
async def test_update_user_view_error():
    controller = MockUserUpdateError()
    view = UserUpdateView(controller)

    http_request = HttpRequest(
        body={
            "username": "Ana",
            "age": 20,
            "uf": "MG",
        },
        path_params={"user_id": 1},
    )

    response = await view.handle_update_user(http_request)

    assert response.status_code == 400
    assert response.body == {"error": "Usuário não encontrado."}