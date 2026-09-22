# Pre-Entrega Automation Testing — Inti Fernández

## Propósito del proyecto

Automatización de pruebas end-to-end sobre [SauceDemo](https://www.saucedemo.com/) usando Selenium WebDriver y Pytest. Cubre tres flujos: login, navegación del catálogo de productos y agregar un producto al carrito, validando en cada caso que la aplicación se comporte como se espera.

## Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- pytest-html (generación de reportes)
- Git / GitHub

## Instalación de dependencias

1. Clonar el repositorio.
2. Instalar las dependencias:
   ```
   pip install selenium pytest pytest-html
   ```
3. Descargar el [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) correspondiente a tu versión de Chrome y colocar el archivo `chromedriver.exe` en la raíz del proyecto.

## Cómo ejecutar las pruebas

Parado en la raíz del proyecto:

```
pytest -v
```

Para generar el reporte HTML:

```
pytest -v --html=reports/reporte.html --self-contained-html
```

El reporte se genera en `reports/reporte.html`.

## Estructura del proyecto

```
├── tests/
│   ├── conftest.py          # fixture del driver de Selenium
│   ├── test_1_login.py
│   ├── test_2_catalogo.py
│   └── test_3_carrito.py
├── utils/
│   └── helpers.py           # función de login reutilizable
├── reports/                 # reportes HTML generados por pytest-html
├── pytest.ini
└── chromedriver.exe
```
