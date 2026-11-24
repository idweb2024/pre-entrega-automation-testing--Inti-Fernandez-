# Pre-Entrega Automation Testing — Inti Fernández

![CI Status](https://github.com/idweb2024/pre-entrega-automation-testing--Inti-Fernandez-/actions/workflows/ci.yml/badge.svg?branch=feature/ci-cd)

## Propósito del proyecto

Automatización de pruebas sobre [SauceDemo](https://www.saucedemo.com/) (interfaz web), [reqres.in](https://reqres.in/) y [JSONPlaceholder](https://jsonplaceholder.typicode.com/) (APIs REST), usando Selenium WebDriver, `requests` y Pytest.

- **UI:** login, navegación del catálogo y carrito de compras, validando en cada caso que la aplicación se comporte como se espera.
- **Page Object Model (POM):** los selectores y acciones de cada pantalla viven en clases dentro de `pages/`, y los tests solo describen el flujo y hacen las validaciones.
- **Data-driven:** los datos de prueba están separados del código, en archivos CSV y JSON dentro de `datos/`, y se usan con `@pytest.mark.parametrize`.
- **API:** pruebas de login, listado y creación de usuarios (reqres.in), y un flujo de ciclo de vida de un post (POST, PATCH y DELETE con datos de Faker en JSONPlaceholder), validando códigos de estado, esquema, tipos y tiempos de respuesta.
- **Reportes y logging:** cada ejecución genera un reporte HTML autocontenido con título y metadatos del proyecto, adjunta una captura de pantalla automática cuando falla un test de UI y registra cada paso de los tests en un log unificado.
- **BDD (Behave):** los flujos de login y carrito están escritos también como historias en Gherkin (`.feature`), legibles por personas no técnicas, y se ejecutan con Behave reutilizando los mismos Page Objects. La suite BDD puede correrse sola o desde Pytest.

## Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- Requests
- Faker (datos de prueba aleatorios)
- Page Object Model (patrón de diseño)
- pytest-html (generación de reportes)
- pytest-rerunfailures (reintentos de tests inestables)
- logging (módulo estándar de Python para el registro de ejecución)
- Behave + Gherkin (BDD: escenarios en lenguaje natural)
- behave-html-formatter (reporte HTML de Behave)
- Git / GitHub

## Instalación de dependencias

1. Clonar el repositorio.
2. Instalar las dependencias desde `requirements.txt`:
   ```
   pip install -r requirements.txt
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
pytest
```

No hace falta agregar opciones: `pytest.ini` ya incluye el modo verbose (`-v`), la generación del reporte HTML y los metadatos del proyecto.

Otras formas de ejecución:

| Qué correr | Comando |
|---|---|
| Solo tests de UI | `pytest tests/` |
| Solo tests de API | `pytest -m api` |
| Solo el flujo de ciclo de vida (e2e) | `pytest -m e2e` |
| Solo tests de humo (smoke) | `pytest -m smoke` |
| Solo la suite BDD (Behave desde Pytest) | `pytest tests_behave/` o `pytest -m bdd` |
| Reintentar los tests que fallen (2 veces, 3 s de pausa) | `pytest --reruns 2 --reruns-delay 3` |

## Ejecutar la suite BDD con Behave

Los escenarios están en `features/` (palabras clave de Gherkin en inglés, texto en español):

- `login.feature` (`@ui`): login exitoso (`@smoke`) y un *Scenario Outline* con tres casos de error (credenciales inválidas, usuario bloqueado y campos vacíos).
- `cart.feature` (`@ui @regression`): login automático en el *Background* y agregar "Sauce Labs Backpack" verificando que el contador del carrito muestre 1.

| Qué correr | Comando |
|---|---|
| Toda la suite BDD | `behave` |
| Solo smoke | `behave -t "@smoke"` |
| Solo regresión | `behave -t "@regression"` |
| Verificar que los pasos estén definidos, sin ejecutar | `behave --dry-run` |
| Suite completa con reportes JSON y HTML | `behave -f json -o reports/behave.json -f html -o reports/behave.html -f pretty` |

En PowerShell los tags van **entre comillas** (`"@smoke"`): sin comillas, PowerShell interpreta el `@` como un operador propio y Behave no recibe el tag.

`behave.ini` define el idioma de Gherkin (`lang = en`), excluye por defecto los escenarios `@wip`, indica la carpeta `features` y registra el formato `html`.

## Reportes y logs

Cada ejecución genera automáticamente:

- **`reports/report.html`:** reporte autocontenido (un solo archivo con CSS, JS e imágenes) con el estado y la duración de cada test, el título del proyecto y una tabla Environment con el autor y el nombre del proyecto. Se reemplaza en cada ejecución.
- **Capturas de pantalla:** cuando falla un test de UI, se guarda una captura en `reports/screens/<nombre_del_test>.png` y además se adjunta dentro del reporte, junto al error.
- **`logs/suite.log`:** registro cronológico de los pasos de los tests de UI, de API y de los escenarios BDD (nivel INFO o superior, con hora). El archivo crece con cada ejecución.
- **Reportes de Behave:** `reports/behave.html` (reporte visual) y `reports/behave.json` (para procesar o integrar en CI). Al ejecutar Behave desde Pytest se generan `reports/behave_smoke.json` y `reports/behave_regression.json`.
- **Capturas de Behave:** si falla un paso, el hook `after_step` guarda una captura en `reports/screens/` con el nombre del paso y la hora.

Ejemplo de `logs/suite.log`:

```
20:19:31 INFO talentolab – Iniciando test de ciclo de vida de un post
20:19:32 INFO talentolab – POST creado con id: 101
20:19:33 INFO talentolab – POST 1.42s | PATCH 0.28s | DELETE 0.28s
```

Los archivos generados no se versionan (están en `.gitignore`): Git solo guarda las carpetas `reports/` y `logs/` vacías, con un `.gitkeep`. Los reportes anteriores que quedaron en `reports/` se conservan como historial de la evolución del proyecto.

## Notas técnicas

- **Aviso de contraseñas de Chrome:** la contraseña pública de SauceDemo (`secret_sauce`) figura en filtraciones de datos, y Chrome muestra un cartel "Cambia tu contraseña" que bloquea la página. La suite BDD abre Chrome con el gestor de contraseñas desactivado (`ChromeOptions` en `features/environment.py`).
- **Reporte HTML de Behave vacío en Windows:** `behave-html-formatter` escribe el reporte pero no cierra el archivo, y en Windows quedaba en 0 bytes. `features/environment.py` aplica una corrección que cierra el archivo al terminar.
- **Escenarios independientes:** como Behave usa un solo navegador para toda la suite, el hook `before_scenario` borra cookies y `localStorage` antes de cada escenario, para que ninguno herede la sesión o el carrito del anterior.

## Estructura del proyecto

```
├── pages/                   # Page Objects: locators y acciones de cada pantalla
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── tests/                   # Tests de UI (Selenium)
│   ├── conftest.py          # fixture del driver y hook de capturas en fallos
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
│   ├── api_utils.py         # URL base y headers (API key) para los tests de API
│   └── logger.py            # logger centralizado que escribe en logs/suite.log
├── features/                # Suite BDD (Behave)
│   ├── login.feature        # escenarios de login (@ui, @smoke)
│   ├── cart.feature         # escenarios de carrito (@ui, @regression)
│   ├── environment.py       # hooks: navegador, sesión limpia, capturas, cierre
│   └── steps/
│       ├── login_steps.py   # pasos de login (usan LoginPage e InventoryPage)
│       └── cart_steps.py    # pasos de carrito (usan LoginPage e InventoryPage)
├── tests_behave/
│   └── test_behave_suite.py # ejecuta Behave desde Pytest (@smoke y @regression)
├── reports/                 # reportes HTML/JSON y capturas (screens/)
├── logs/                    # log de ejecución (suite.log)
├── conftest.py              # hook que define el título del reporte
├── pytest.ini               # opciones por defecto, reporte HTML, metadatos y markers (smoke, api, e2e, bdd, regression)
├── behave.ini               # configuración de Behave (idioma, tags por defecto, ruta, formato html)
├── requirements.txt         # dependencias del proyecto
└── .gitignore
```
