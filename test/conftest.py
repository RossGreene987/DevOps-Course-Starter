import pytest as pytest
from dotenv import load_dotenv, find_dotenv

from todo_app.app import create_app


@pytest.fixture
def client():
    load_dotenv(find_dotenv(".env.test"), override=True)
    test_app = create_app()
    with test_app.test_client() as client:
        yield client
