import pytest
from fastapi.testclient import TestClient

from aprendendo_fastapi.app import app


@pytest.fixture
def client():
    return TestClient(app)
