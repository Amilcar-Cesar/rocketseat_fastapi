import pytest

from .http_types.http_request import HttpRequest
from .user_delete_view import UserDeleteView


class MockUserDelete:
    def __init__(self):
        self.delete_user_att = {}

    async def delete_user(self, user_id: int) -> dict:
        self.delete_user_att = {
            "user_id": user_id,
        }
        return {
            "type": "users",
            "count": 1,
            "message": "Usuário deletado com sucesso.",
        }
    
class MockUserDeleteError:
    async def delete_user(self, user_id: int) -> dict:
        raise Exception("Usuário não encontrado.")
    
@pytest.mark.asyncio
async def test_delete_user_view():
    controller = MockUserDelete()
    view = UserDeleteView(controller)

    user_id = 1

    http_request = HttpRequest(
        path_params={"user_id": user_id},
    )

    response = await view.handle_delete_user(http_request)

    assert controller.delete_user_att["user_id"] == user_id

    assert response.status_code == 200
    assert response.body["type"] == "users"
    assert response.body["count"] == 1
    assert response.body["message"] == "Usuário deletado com sucesso."

@pytest.mark.asyncio
async def test_delete_user_view_error():
    controller = MockUserDeleteError()
    view = UserDeleteView(controller)

    user_id = 1

    http_request = HttpRequest(
        path_params={"user_id": user_id},
    )

    response = await view.handle_delete_user(http_request)

    assert response.status_code == 404
    assert response.body["error"] == "Usuário não encontrado."