from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import pytest

@pytest.mark.smoke
def test_carrito(driver):
    # 1) Login
    login_page = LoginPage(driver)
    login_page.abrir().login_completo("standard_user", "secret_sauce")

    # 2) Inventario: guardar nombre y precio del primer producto ANTES de agregarlo
    inventory_page = InventoryPage(driver)
    nombre = inventory_page.obtener_nombres()[0]
    precio = inventory_page.obtener_precios()[0]


    # 3) Agregar al carrito y verificar el contador
    inventory_page.agregar_primer_producto()
    assert inventory_page.obtener_contador_carrito() == 1

    # 4) Ir al carrito (devuelve un CartPage)
    cart_page = inventory_page.ir_al_carrito()

     # 5) Verificar los datos del producto en el carrito
    assert cart_page.obtener_cantidad() == "1"
    assert cart_page.obtener_nombre() == nombre
    assert cart_page.obtener_descripcion() != ""
    assert cart_page.obtener_precio() == precio


  
