from .users_repository import UsersRepository
import pytest


@pytest.mark.asyncio
@pytest.mark.skip(reason="Insert in DB")
async def test_insert_user():
    new_user = {
        "username": "test_user",
        "age": 30,
        "uf": "SP"
    }

    repo = UsersRepository()
    await repo.insert_user(new_user)

@pytest.mark.asyncio
@pytest.mark.skip(reason="Select in DB")
async def test_get_user_by_username():
    repo = UsersRepository()
    response = await repo.get_user_by_username("test_user")
    print(response)
