from behave import given, when, then

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger


@given('que inicié sesión con usuario "{usuario}" y clave "{clave}"')
def step_login_automatico(context, usuario, clave):
    logger.info("Login automático con usuario: %s", usuario)
    LoginPage(context.driver).abrir().login_completo(usuario, clave)
    context.inventory_page = InventoryPage(context.driver)


@when('agrego el producto "{producto}" al carrito')
def step_agregar_producto(context, producto):
    logger.info("Agregando al carrito: %s", producto)
    context.inventory_page.agregar_producto(producto)


@then('el contador del carrito muestra "{cantidad:d}"')
def step_verificar_contador(context, cantidad):
    logger.info("Verificando que el contador muestre: %s", cantidad)
    contador = context.inventory_page.obtener_contador_carrito()
    assert contador == cantidad, f"El contador muestra {contador}, se esperaba {cantidad}"