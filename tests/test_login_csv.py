import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.datos import leer_csv_login

CASOS_LOGIN = leer_csv_login("datos/login.csv")

@pytest.mark.parametrize("usuario, clave, debe_funcionar, descripcion", CASOS_LOGIN)
def test_login_desde_csv(driver, usuario, clave, debe_funcionar, descripcion):
    login_page = LoginPage(driver)
    login_page.abrir().login_completo(usuario, clave)

    if debe_funcionar:
        inventory_page = InventoryPage(driver)
        titulo = inventory_page.obtener_titulo()
        assert "/inventory.html" in driver.current_url
        assert "products" in titulo.lower()
    else:
        assert login_page.esta_error_visible()
    

@pytest.mark.smoke
def test_login_usuario_valido_smoke(driver):
    """Smoke: verifica que al menos un login válido funciona."""
    LoginPage(driver).abrir().login_completo("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)

    assert "/inventory.html" in driver.current_url
    assert "products" in inventory_page.obtener_titulo().lower()