from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import pytest
from utils.logger import logger

@pytest.mark.smoke
def test_login(driver):
    logger.info("Iniciando prueba de login")
    login_page = LoginPage(driver)
    
    logger.info("Abriendo login e ingresando con usuario: %s", "standard_user")
    login_page.abrir().login_completo("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    titulo = inventory_page.obtener_titulo()
    
    logger.info("Verificando la url de la pagina de inventario")
    assert "/inventory.html" in driver.current_url
    logger.info("Verificando el titulo de la pagina de inventario")
    assert "products" in titulo.lower()
    logger.info("Test de login completado")