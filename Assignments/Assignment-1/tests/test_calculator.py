from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_add():
    response = client.get("/calculator/add?a=5&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 8}
