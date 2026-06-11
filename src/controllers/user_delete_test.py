from .user_delete import UserDelete
import pytest

class UserRepositoryMock():
    def __init__(self):
        self.delete_user_att = {}

    def get_user_by_id(self, user_id: int):
        return {"user_id": user_id}
    
    async def delete_user(self, user_id: int) -> None:
        self.delete_user_att = {"user_id": user_id}
        return None
    
@pytest.mark.asyncio
async def test_delete_user():
    user_repository = UserRepositoryMock()
    user_delete = UserDelete(user_repository)

    user_id = 1

    response = await user_delete.delete_user(user_id)

    assert user_repository.delete_user_att["user_id"] == user_id

    assert response["type"] == "users"
    assert response["count"] == 1
    assert response["message"] == f"Usuário com id {user_id} deletado com sucesso."
    print(response)