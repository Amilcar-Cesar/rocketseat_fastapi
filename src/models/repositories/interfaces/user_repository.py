from abc import ABC, abstractmethod

class UsersRepositoryInterface(ABC):
    @abstractmethod
    async def insert_user(self, user_infos: dict) -> None:
        pass

    @abstractmethod
    async def get_user_by_username(self, username: str) ->list[dict]:
        pass
        
    @abstractmethod
    async def update_user(self, user_id: int, updated_infos: dict) -> None:
        pass
    
    @abstractmethod
    async def delete_user(self, user_id: int) -> None:
        pass