import pathlib
import re
from datetime import datetime

from selenium import webdriver
from utils.logger import logger
import os

SCREEN_DIR = pathlib.Path('reports/screens')
SCREEN_DIR.mkdir(parents=True, exist_ok=True)

def before_all(context):
    """Abre el navegador una sola vez para toda la suite."""
    opciones = webdriver.ChromeOptions()
    opciones.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })
    if os.environ.get("CI"):
        opciones.add_argument("--headless=new")
        opciones.add_argument("--no-sandbox")
        opciones.add_argument("--disable-dev-shm-usage")
        opciones.add_argument("--window-size=1920,1080")
    context.driver = webdriver.Chrome(options=opciones)
    if not os.environ.get("CI"):
        context.driver.maximize_window()
    logger.info("Behave: navegador iniciado")

def before_scenario(context, scenario):
    """Arranca cada escenario con la sesión limpia."""
    logger.info("Iniciando escenario: %s", scenario.name)
    context.driver.delete_all_cookies()
    try:
        context.driver.execute_script("window.localStorage.clear();")
    except Exception:
        pass  # en la primera página (vacía) no hay localStorage


def after_step(context, step):
    """Si un paso falla, guarda una captura en reports/screens/."""
    if step.status in ('failed', 'error') and hasattr(context, 'driver'):
        nombre = re.sub(r'[^\w-]', '_', step.name)
        hora = datetime.now().strftime('%H%M%S')
        archivo = SCREEN_DIR / f"{nombre}_{hora}.png"
        context.driver.save_screenshot(str(archivo))
        logger.error("Paso fallido: %s - captura en %s", step.name, archivo)


def after_all(context):
    """Cierra el navegador al terminar toda la suite."""
    if hasattr(context, 'driver'):
        context.driver.quit()
        logger.info("Behave: navegador cerrado")


# --- Corrección del bug de behave-html-formatter ---
# El plugin escribe el reporte HTML pero nunca cierra el archivo,
# y en Windows queda vacío. Le agregamos el cierre que le falta.
from behave_html_formatter import HTMLFormatter

_cerrar_original = HTMLFormatter.close


def _cerrar_y_guardar(self):
    _cerrar_original(self)   # lo que ya hacía: escribir el HTML
    self.close_stream()      # lo que le faltaba: cerrar el archivo


HTMLFormatter.close = _cerrar_y_guardar