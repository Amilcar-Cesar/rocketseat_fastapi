from .user_register import UserRegister
import pytest

class UserRepositoryMock():
    def __init__(self):
        self.insert_users_att = {}
    
    async def insert_user(self, user_infos: dict) -> None:
        self.insert_users_att["user_infos"] = user_infos

@pytest.mark.asyncio
async def test_register_users():
    user_repository = UserRepositoryMock()
    user_register = UserRegister(user_repository)

    user_info = {
        "username": "Maria Eduarda",
        "age": 32,
        "uf": "MG"
    }

    response = await user_register.register_user(user_info)
    
    assert user_repository.insert_users_att["user_infos"] == user_info

    assert response["type"] == "users"
    assert response["count"] == 1
    assert response["attributes"] == user_info

@pytest.mark.asyncio
async def test_register_users_error_uf():
    user_repository = UserRepositoryMock()
    user_register = UserRegister(user_repository)

    invalid_uf_user_info = {
        "username": "Maria Eduarda",
        "age": 32,
        "uf": "ES"
    }

    with pytest.raises(Exception) as excinfo:
        await user_register.register_user(invalid_uf_user_info)

    assert str(excinfo.value) == "Estado inválido para cadastro."
    assert user_repository.insert_users_att == {}

@pytest.mark.asyncio
async def test_register_users_error_age():
    user_repository = UserRepositoryMock()
    user_register = UserRegister(user_repository)

    invalid_age_user_info = {
        "username": "Maria Eduarda",
        "age": 151,
        "uf": "MG"
    }

    with pytest.raises(Exception) as excinfo:
        await user_register.register_user(invalid_age_user_info)

    assert str(excinfo.value) == "Idade inválida para cadastro."
    assert user_repository.insert_users_att == {}