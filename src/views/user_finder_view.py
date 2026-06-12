from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.controllers.interfaces.user_finder import UserFinderInterface

class UserFinderView:
    def __init__(self, controller: UserFinderInterface) -> None:
        self.__controller = controller

    async def handle_find_user(self, http_request: HttpRequest) -> HttpResponse:
        try:
            username = http_request.path_params["username"]
            response = await self.__controller.get_user_by_username(username)
            return HttpResponse(body=response, status_code=200)
        except Exception as e:
            return HttpResponse(body={"error": str(e)}, status_code=500)