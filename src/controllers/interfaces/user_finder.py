from abc import ABC, abstractmethod

class UserFinderInterface(ABC):

    @abstractmethod
    async def get_user_by_username(self, username: str) -> dict:
        pass