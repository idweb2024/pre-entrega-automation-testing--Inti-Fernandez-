from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import pytest
@pytest.mark.smoke
def test_catalogo(driver):
    login_page = LoginPage(driver)
    login_page.abrir().login_completo("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver)
    titulo = inventory_page.obtener_titulo()
    assert titulo == "Products"

    productos = inventory_page.obtener_nombres()
    assert len(productos) > 0

    nombre = productos[0]
    assert nombre != ""
    print("Primer producto →", nombre)

    precio = inventory_page.obtener_precios()[0]
    print("Precio →", precio)






