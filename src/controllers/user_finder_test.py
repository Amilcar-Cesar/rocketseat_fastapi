
import pytest
from .user_finder import UserFinder

class UserRepositoryMock():
    def __init__(self):
        self.insert_users_att = {}

    async def get_user_by_username(self, username: str) -> list[dict]:
        self.get_user_by_username_att = {"username": username}
        return [{"username": "ola"}, {"username": "mundo"}]
    
@pytest.mark.asyncio
async def test_find_user_by_username():
    user_repository = UserRepositoryMock()
    user_finder = UserFinder(user_repository)

    username = "Ana"
    response = await user_finder.get_user_by_username(username)

    assert user_repository.get_user_by_username_att["username"] == username

    assert response["type"] == "users"
    assert response["count"] == 2
    assert "attributes" in response
    assert isinstance(response["attributes"], list)
    assert isinstance(response["attributes"][0], dict)
    print(response["message"])