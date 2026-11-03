import pytest
import requests
import time
from faker import Faker
from utils.logger import logger

URL = "https://jsonplaceholder.typicode.com/posts"

# Va todo en un solo test (Flujo encadenado)
@pytest.mark.e2e
@pytest.mark.api
def test_post_lifecycle(): 
    logger.info("Iniciando test de ciclo de vida de un post")
    inicio = time.time() # Cronometro
    fake = Faker() # Generador de datos falsos

    sesion = requests.Session() # Objeto de sesion (Rehuso la conexión en una sola sesión)

    payload = {
        "title": fake.sentence(),
        "body": fake.paragraph(),
        "userId": 1
    }

    # POST
    logger.info("Enviando POST a %s", URL)
    response = sesion.post(URL, json=payload)
    r = response.json()

    post_id = r["id"]
    logger.info("POST creado con id: %s", post_id)

    logger.info("Verificando respuesta 201")
    assert response.status_code == 201

    logger.info("Verificando que el ID sea un entero")
    assert isinstance(post_id, int)

    logger.info("Verificando TITULO del payload")
    assert r["title"] == payload["title"]
    logger.info("Verificando BODY del payload")
    assert r["body"] == payload["body"]
    logger.info("Verificando USER ID del payload")
    assert r["userId"] == payload["userId"]

    # PATCH
    url_post = f"{URL}/{post_id}"
    nuevo_titulo = "Título actualizado por QA"

    logger.info("PATCH a %s con título: %s", url_post, nuevo_titulo)
    response_patch = sesion.patch(url_post, json={"title": nuevo_titulo})
    
    logger.info("Verificando respuesta 200")
    assert response_patch.status_code == 200
    logger.info("Verificando TITULO actualizado")
    assert response_patch.json()["title"] == nuevo_titulo

    # DELETE
    logger.info("DELETE a %s", url_post)
    response_delete = sesion.delete(url_post)

    logger.info("Verificando respuesta 200")
    assert response_delete.status_code == 200

    # Verificar cronometro
    fin = time.time()
    duracion = fin - inicio
    # Modificando los print para capturarlos en el logger
    logger.info("Tiempo de ejecucion: %.2fs", duracion)
    logger.info("POST %.2fs | PATCH %.2fs | DELETE %.2fs",
               response.elapsed.total_seconds(),
               response_patch.elapsed.total_seconds(),
               response_delete.elapsed.total_seconds())
    
    logger.info("Verificando que el tiempo de ejecucion sea menor a 3s")
    assert duracion < 3

    logger.info("Test de ciclo de vida de un post completado")