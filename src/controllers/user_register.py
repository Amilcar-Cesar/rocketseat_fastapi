from src.models.repositories.interfaces.user_repository import UsersRepositoryInterface

class UserRegister():
    def __init__(self, user_repository: UsersRepositoryInterface):
        self.__user_repository = user_repository
        
    async def register_user(self, user_data: dict) -> dict:
        self.__validate_user_data(user_data)
        await self.__registry_user(user_data)
        return self.format_response(user_data)

    def __validate_user_data(self, user_data: dict) -> None:
        age = user_data["age"]
        uf = user_data["uf"]

        if uf not in ["MG", "BA", "CE", "SC", "MT"]:
            raise Exception("Estado inválido para cadastro.")
        
        if age < 0 or age > 150:
            raise Exception("Idade inválida para cadastro.")
        
    async def __registry_user(self, user_data: dict) -> None:
        await self.__user_repository.insert_user(user_data)

    def format_response(self, user_data: dict) -> dict:
        return {
            "type" : "users",
            "count": 1,
            "message": "Usuário cadastrado com sucesso.",
            "attributes": user_data
        }