from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import pytest

@pytest.mark.smoke
def test_login(driver):
    login_page = LoginPage(driver)
    login_page.abrir().login_completo("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    titulo = inventory_page.obtener_titulo()

    assert "/inventory.html" in driver.current_url
    assert "products" in titulo.lower()