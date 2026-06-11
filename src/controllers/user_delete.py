from src.models.repositories.interfaces.user_repository import UsersRepositoryInterface

class UserDelete():
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.users_repository = users_repository

    async def delete_user(self, user_id: int) -> dict:
        self.__validate_user_id(user_id)
        await self.users_repository.delete_user(user_id)
        return self.format_response(user_id)
    
    def __validate_user_id(self, user_id: int) -> None:
        user = self.users_repository.get_user_by_id(user_id)
        if not user:
            raise Exception("Usuário não encontrado.")
        
    def format_response(self, user_id: int) -> dict:
        return {
            "type" : "users",
            "count": 1,
            "message": f"Usuário com id {user_id} deletado com sucesso.",
        }