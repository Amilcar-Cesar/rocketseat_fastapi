from src.models.repositories.interfaces.user_repository import UsersRepositoryInterface
from .interfaces.user_update import UserUpdateInterface

class UserUpdate(UserUpdateInterface):
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.users_repository = users_repository

    async def update_user(self, user_id: int, updated_infos: dict) -> dict:
        self.__validate_user_id(user_id)
        self.__validate_user_data(updated_infos)
        await self.users_repository.update_user(user_id, updated_infos)
        return self.format_response(updated_infos)
    
    def __validate_user_id(self, user_id: int) -> None:
        user = self.users_repository.get_user_by_id(user_id)
        if not user:
            raise Exception("Usuário não encontrado.")

    def __validate_user_data(self, updated_infos: dict) -> None:
        age = updated_infos["age"]
        uf = updated_infos["uf"]

        if uf not in ["MG", "BA", "CE", "SC", "MT"]:
            raise Exception("Estado inválido para cadastro.")
        
        if age < 0 or age > 150:
            raise Exception("Idade inválida para cadastro.")
        
    def format_response(self, updated_infos: dict) -> dict:
        return {
            "type" : "users",
            "count": 1,
            "message": "Usuário atualizado com sucesso.",
            "attributes": updated_infos
        }