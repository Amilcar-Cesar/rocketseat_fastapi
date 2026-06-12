from abc import ABC, abstractmethod

class UserUpdateInterface(ABC):

    @abstractmethod
    async def update_user(self, user_id: int, updated_infos: dict) -> dict:
        pass