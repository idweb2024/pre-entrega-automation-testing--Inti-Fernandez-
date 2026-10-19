import os

BASE_URL = "https://reqres.in/api"


def obtener_headers():
    """Devuelve los headers con la API key leída de la variable de entorno."""
    return {"x-api-key": os.environ["REQRES_API_KEY"]}