from src.models.repositories.users_repository import UsersRepository
from src.controllers.user_update import UserUpdate
from src.views.user_update_view import UserUpdateView

def user_update_composer():
    model= UsersRepository()
    controller = UserUpdate(model)
    view = UserUpdateView(controller)

    return view