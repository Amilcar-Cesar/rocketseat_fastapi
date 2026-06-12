from abc import ABC, abstractmethod

class UserDeleteInterface(ABC):

    @abstractmethod
    async def delete_user(self, user_id: int) -> dict:
        pass