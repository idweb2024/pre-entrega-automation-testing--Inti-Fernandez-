# Pre-Entrega Automation Testing — Inti Fernández

## Propósito del proyecto

Automatización de pruebas sobre [SauceDemo](https://www.saucedemo.com/) (interfaz web), [reqres.in](https://reqres.in/) y [JSONPlaceholder](https://jsonplaceholder.typicode.com/) (APIs REST), usando Selenium WebDriver, `requests` y Pytest.

- **UI:** login, navegación del catálogo y carrito de compras, validando en cada caso que la aplicación se comporte como se espera.
- **Page Object Model (POM):** los selectores y acciones de cada pantalla viven en clases dentro de `pages/`, y los tests solo describen el flujo y hacen las validaciones.
- **Data-driven:** los datos de prueba están separados del código, en archivos CSV y JSON dentro de `datos/`, y se usan con `@pytest.mark.parametrize`.
- **API:** pruebas de login, listado y creación de usuarios (reqres.in), y un flujo de ciclo de vida de un post (POST, PATCH y DELETE con datos de Faker en JSONPlaceholder), validando códigos de estado, esquema, tipos y tiempos de respuesta.

## Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- Requests
- Faker (datos de prueba aleatorios)
- Page Object Model (patrón de diseño)
- pytest-html (generación de reportes)
- Git / GitHub

## Instalación de dependencias

1. Clonar el repositorio.
2. Instalar las dependencias:
   ```
   pip install selenium pytest pytest-html requests faker
   ```
3. Tener Google Chrome instalado. Selenium descarga automáticamente el ChromeDriver compatible con tu versión de Chrome, así que no hace falta bajarlo a mano (la primera ejecución necesita conexión a internet).
4. **Solo para los tests de reqres.in (login, usuarios, creación):** reqres.in exige una API key en cada pedido.
   - Crear una cuenta gratuita en [app.reqres.in](https://app.reqres.in/) y copiar una clave.
   - El test de ciclo de vida (JSONPlaceholder) no necesita clave.
   - Guardarla en la variable de entorno `REQRES_API_KEY` (nunca dentro del código):

     Windows (PowerShell), de forma permanente. Después, abrir una terminal nueva:
     ```
     setx REQRES_API_KEY "tu_clave"
     ```
     macOS / Linux:
     ```
     export REQRES_API_KEY="tu_clave"
     ```

## Cómo ejecutar las pruebas

Parado en la raíz del proyecto:

```
pytest -v
```

Otras formas de ejecución:

| Qué correr | Comando |
|---|---|
| Solo tests de UI | `pytest tests/ -v` |
| Solo tests de API | `pytest -m api -v` |
| Solo el flujo de ciclo de vida (e2e) | `pytest -m e2e -v` |
| Solo tests de humo (smoke) | `pytest -m smoke -v` |
| UI + API | `pytest tests/ tests_api/ -v` |

Para generar el reporte HTML con todos los tests:

```
pytest tests/ tests_api/ -v --html=reports/reporte_completo.html --self-contained-html
```

El reporte se genera en `reports/reporte_completo.html`.

## Estructura del proyecto

```
├── pages/                   # Page Objects: locators y acciones de cada pantalla
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── tests/                   # Tests de UI (Selenium)
│   ├── conftest.py          # fixture del driver
│   ├── test_1_login.py
│   ├── test_2_catalogo.py
│   ├── test_3_carrito.py
│   ├── test_login_csv.py    # login parametrizado con datos/login.csv
│   └── test_carrito_json.py # carrito parametrizado con datos/productos.json
├── tests_api/               # Tests de API (requests)
│   ├── __init__.py
│   ├── test_login_api.py
│   ├── test_users_api.py
│   ├── test_create_user_api.py
│   └── test_post_lifecycle.py  # POST → PATCH → DELETE con Faker
├── datos/                   # Datos de prueba externos
│   ├── login.csv
│   └── productos.json
├── utils/
│   ├── helpers.py           # función de login reutilizable
│   ├── datos.py             # lectura de CSV y JSON
│   └── api_utils.py         # URL base y headers (API key) para los tests de API
├── reports/                 # reportes HTML generados por pytest-html
└── pytest.ini               # configuración de Pytest y markers (smoke, api, e2e)
```