import pytest
import requests
from utils.api_utils import BASE_URL, obtener_headers

CASOS_LOGIN = [
    ({"email": "eve.holt@reqres.in", "password": "cityslicka"}, 200, True),
    ({"email": "eve.holt@reqres.in"}, 400, False),
]


@pytest.mark.api
@pytest.mark.parametrize("payload, status_esperado, debe_tener_token", CASOS_LOGIN)
def test_login_api(payload, status_esperado, debe_tener_token):
    url = f"{BASE_URL}/login"
    response = requests.post(url, json=payload, headers=obtener_headers())
    assert response.status_code == status_esperado

    if debe_tener_token:
        assert "token" in response.json()