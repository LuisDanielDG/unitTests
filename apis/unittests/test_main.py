import requests
import pytest

URI_BASE="http://localhost:8000"

def test_red_root():
    url = f"{URI_BASE}/"
    response = requests.get(url)
    assert response.status_code == 202
    assert response.json() == {"message": "Pruebas unitarias"}

def test_sumas():
    url = f"{URI_BASE}/sumas"
    params = {"numero1": 5, "numero2": 10}
    response = requests.get(url, params=params)
    assert response.status_code == 202
    assert response.json() == {
        "numero1": 5,
        "numero2": 10,
        "suma": 15
    }

def test_restas():
    url = f"{URI_BASE}/restas"
    params = {"numero1": 15, "numero2": 5}
    response = requests.get(url, params=params)
    assert response.status_code == 202
    assert response.json() == {
        "numero1": 15,
        "numero2": 5,
        "resta": 10
    }

def test_multiplicaciones():
    url = f"{URI_BASE}/multiplicaciones"
    params = {"numero1": 4, "numero2": 5}
    response = requests.get(url, params=params)
    assert response.status_code == 202
    assert response.json() == {
        "numero1": 4,
        "numero2": 5,
        "multiplicacion": 20
    }

def test_divisiones():
    url = f"{URI_BASE}/divisiones"
    params = {"numero1": 20, "numero2": 5}
    response = requests.get(url, params=params)
    assert response.status_code == 202
    assert response.json() == {
        "numero1": 20,
        "numero2": 5,
        "division": 4.0
    }
