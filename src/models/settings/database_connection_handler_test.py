import pytest
from .database_connection_handler import DBConnectionHandler

@pytest.mark.asyncio
@pytest.mark.skip(reason="Connection to DB")
async def test_connection():
    async with DBConnectionHandler() as db_handler:
        print(db_handler.session)
        assert  db_handler.session is not None