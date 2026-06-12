import pytest
from .user_finder_view import UserFinderView
from .http_types.http_request import HttpRequest

class MockUserFinder:
    def __init__(self):
        self.find_user_att = {}

    async def get_user_by_username(self, username: str) -> dict:
        self.find_user_att = {
            "username": username,
        }
        return {
            "type": "users",
            "count": 1,
            "message": "Usuário encontrado com sucesso.",
            "attributes": {
                "username": f"{username}",
                "age": 20,
                "uf": "MG",
            },
        }

class MockUserFinderError:
    async def get_user_by_username(self, username: str) -> dict:
        raise Exception("Usuário não encontrado.")
    
@pytest.mark.asyncio
async def test_find_user_view():
    controller = MockUserFinder()
    view = UserFinderView(controller)
    
    username = "Ana"

    http_request = HttpRequest(
        path_params={"username": username},
    )

    response = await view.handle_find_user(http_request)

    assert controller.find_user_att["username"] == username

    assert response.status_code == 200
    assert response.body["type"] == "users"
    assert response.body["count"] == 1
    assert response.body["attributes"]["username"] == "Ana"
    assert response.body["attributes"]["age"] == 20
    assert response.body["attributes"]["uf"] == "MG"

@pytest.mark.asyncio
async def test_find_user_view_error():
    controller = MockUserFinderError()
    view = UserFinderView(controller)
    
    username = "Ana"

    http_request = HttpRequest(
        path_params={"username": username},
    )

    response = await view.handle_find_user(http_request)

    assert response.status_code == 500
    assert "error" in response.body
