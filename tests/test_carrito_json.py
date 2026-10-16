import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.datos import leer_json_productos

PRODUCTOS = leer_json_productos("datos/productos.json")


@pytest.fixture
def usuario_logueado(driver):
    """Hace login con el usuario válido y devuelve la página de inventario lista."""
    LoginPage(driver).abrir().login_completo("standard_user", "secret_sauce")
    return InventoryPage(driver)


@pytest.mark.parametrize("producto", PRODUCTOS, ids=[p["nombre"] for p in PRODUCTOS]) # list comprehension
def test_agregar_producto_desde_json(usuario_logueado, producto):
    inventory_page = usuario_logueado

    inventory_page.agregar_producto(producto["nombre"])
    assert inventory_page.obtener_contador_carrito() == 1

    cart_page = inventory_page.ir_al_carrito()

    assert cart_page.obtener_cantidad() == "1"
    assert cart_page.obtener_nombre() == producto["nombre"]
    assert cart_page.obtener_precio() == f"${producto['precio']:.2f}"


@pytest.mark.smoke
def test_carrito_smoke(usuario_logueado):
    usuario_logueado.agregar_primer_producto()
    assert usuario_logueado.obtener_contador_carrito() == 1