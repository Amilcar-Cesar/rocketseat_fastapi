from sqlalchemy import insert, select, update, delete
from src.models.entities.users import Users
from src.models.settings.database_connection_handler import DBConnectionHandler
from src.models.repositories.interfaces.user_repository import UsersRepositoryInterface

class UsersRepository(UsersRepositoryInterface):
    async def insert_user(self, user_infos: dict) -> None:
        async with DBConnectionHandler() as db:
            query = insert(Users).values(**user_infos)
            await db.session.execute(query)
            await db.session.commit()

    async def get_user_by_username(self, username: str) ->list[dict]:
        async with DBConnectionHandler()as db:
            query = (
                select(Users)
                .where(Users.c.username == username)
            )
            result = await db.session.execute(query)
            rows = result.fetchall()

            users_list = [dict(row._mapping) for row in rows]
            return users_list
        
    async def update_user(self, user_id: int, updated_infos: dict) -> None:
        async with DBConnectionHandler() as db:
            query = (
                update(Users)
                .where(Users.c.id == user_id)
                .values(**updated_infos)
            )
            await db.session.execute(query)
            await db.session.commit()

    async def delete_user(self, user_id: int) -> None:
        async with DBConnectionHandler() as db:
            query = (
                delete(Users)
                .where(Users.c.id == user_id)
            )
            await db.session.execute(query)
            await db.session.commit()