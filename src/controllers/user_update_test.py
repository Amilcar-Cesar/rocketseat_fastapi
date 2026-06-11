from .user_update import UserUpdate
import pytest

class UserRepositoryMock():
    def __init__(self):
        self.update_user_att = {}

    def get_user_by_id(self, user_id: int):
        return {"user_id": user_id}

    async def update_user(self, user_id: int, updated_infos: dict) -> dict:
        self.update_user_att = {"user_id": user_id, "updated_infos": updated_infos}
        return {"user_id": user_id, **updated_infos}
    
@pytest.mark.asyncio
async def test_update_user():
    user_repository = UserRepositoryMock()
    user_update = UserUpdate(user_repository)

    user_id = 1
    updated_infos = {
        "username": "Ana",
        "age": 20,
        "uf": "MG"
    }

    response = await user_update.update_user(user_id, updated_infos)

    assert user_repository.update_user_att["user_id"] == user_id
    assert user_repository.update_user_att["updated_infos"] == updated_infos

    assert response["type"] == "users"
    assert response["count"] == 1
    assert response["attributes"] == updated_infos
    print(response)