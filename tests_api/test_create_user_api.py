import pytest
import requests
from datetime import datetime
from utils.api_utils import BASE_URL, obtener_headers

DATOS = [
    ("Fernando", "QA"),
    ("Luis", "Developer"),
    ("Andrea", "Devops"),
]


@pytest.mark.api
@pytest.mark.parametrize("nombre, trabajo", DATOS)
def test_create_user_api(nombre, trabajo):
    url = f"{BASE_URL}/users"
    payload = {"name": nombre, "job": trabajo}
    response = requests.post(url, json=payload, headers=obtener_headers())
    usuario = response.json()

    assert response.status_code == 201
    assert usuario["name"] == nombre
    assert usuario["job"] == trabajo
    assert "id" in usuario and "createdAt" in usuario
    assert str(datetime.now().year) in usuario["createdAt"]