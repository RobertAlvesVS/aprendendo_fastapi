import pytest
from fastapi.testclient import TestClient

from aprendendo_fastapi import app


@pytest.fixture
def client():
    return TestClient(app)
