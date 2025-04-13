from fastapi.testclient import TestClient
from application.main import app

def test_get_all_intervals():
    with TestClient(app) as client:
        response = client.get("/producers/intervals")
        assert response.status_code == 200
        data = response.json()
        assert "min" in data
        assert "max" in data

def test_get_min_interval():
    with TestClient(app) as client:
        response = client.get("/producers/intervals/min")
        assert response.status_code == 200

def test_get_max_interval():
    with TestClient(app) as client:
        response = client.get("/producers/intervals/max")
        assert response.status_code == 200
