from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.controllers.interfaces.user_update import UserUpdateInterface

class UserUpdateView:
    def __init__(self, controller: UserUpdateInterface) -> None:
        self.__controller = controller

    async def handle_update_user(self, http_request: HttpRequest) -> HttpResponse:
        try:
            user_id = http_request.path_params["user_id"]
            user_data = http_request.body
            response = await self.__controller.update_user(user_id, user_data)
            return HttpResponse(body=response, status_code=200)
        except Exception as e:
            return HttpResponse(body={"error": str(e)}, status_code=400)