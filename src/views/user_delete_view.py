from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.controllers.interfaces.user_delete import UserDeleteInterface

class UserDeleteView:
    def __init__(self, controller: UserDeleteInterface) -> None:
        self.__controller = controller

    async def handle_delete_user(self, http_request: HttpRequest) -> HttpResponse:
        try:
            user_id = http_request.path_params["user_id"]
            response = await self.__controller.delete_user(user_id)
            return HttpResponse(body=response, status_code=200)
        except Exception as e:
            return HttpResponse(body={"error": str(e)}, status_code=404)