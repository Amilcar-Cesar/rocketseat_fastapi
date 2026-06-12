from src.models.repositories.interfaces.user_repository import UsersRepositoryInterface
from .interfaces.user_finder import UserFinderInterface

class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.users_repository = users_repository

    async def get_user_by_username(self, username: str) -> dict:
        users = await self.users_repository.get_user_by_username(username)
        return {
            "type": "users",
            "count": len(users),
            "message": f"{len(users)} usuário(s) encontrado(s) com o username '{username}'.",
            "attributes": users
        }