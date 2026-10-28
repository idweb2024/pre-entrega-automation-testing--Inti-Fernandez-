import pytest
import requests
import time
from faker import Faker

URL = "https://jsonplaceholder.typicode.com/posts"

# Va todo en un solo test (Flujo encadenado)
@pytest.mark.e2e
@pytest.mark.api
def test_post_lifecycle(): 
    inicio = time.time() # Cronometro
    fake = Faker() # Generador de datos falsos

    sesion = requests.Session() # Objeto de sesion (Rehuso la conexión en una sola sesión)
    
    payload = {
        "title": fake.sentence(),
        "body": fake.paragraph(),
        "userId": 1
    }

    # POST
    response = sesion.post(URL, json=payload)
    r = response.json()
    post_id = r["id"]
    assert response.status_code == 201

    assert isinstance(post_id, int)
    assert r["title"] == payload["title"]
    assert r["body"] == payload["body"]
    assert r["userId"] == payload["userId"]

    # PATCH
    url_post = f"{URL}/{post_id}"
    nuevo_titulo = "Título actualizado por QA"
    response_patch = sesion.patch(url_post, json={"title": nuevo_titulo})
    assert response_patch.status_code == 200
    assert response_patch.json()["title"] == nuevo_titulo

    # DELETE
    response_delete = sesion.delete(url_post)
    assert response_delete.status_code == 200

    # Verificar cronometro
    fin = time.time()
    duracion = fin - inicio
    print(f"Tiempo de ejecucion: {duracion}")
    print(f"POST {response.elapsed.total_seconds():.2f}s | PATCH {response_patch.elapsed.total_seconds():.2f}s | DELETE {response_delete.elapsed.total_seconds():.2f}s")
    assert duracion < 3