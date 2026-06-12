from src.models.repositories.users_repository import UsersRepository
from src.controllers.user_delete import UserDelete
from src.views.user_delete_view import UserDeleteView

def user_delete_composer():
    model= UsersRepository()
    controller = UserDelete(model)
    view = UserDeleteView(controller)

    return view