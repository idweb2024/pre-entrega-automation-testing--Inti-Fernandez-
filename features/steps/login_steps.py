import parse
from behave import given, when, then, register_type

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger


# Tipo de parámetro que acepta texto vacío (para el caso "campos vacíos")
@parse.with_pattern(r'[^"]*')
def parse_texto(texto):
    return texto

register_type(Texto=parse_texto)


@given('que estoy en la página de login')
def step_abrir_login(context):
    logger.info("Abriendo la página de login")
    context.login_page = LoginPage(context.driver).abrir()


@when('ingreso usuario "{usuario:Texto}" y clave "{clave:Texto}"')
def step_ingresar_credenciales(context, usuario, clave):
    logger.info("Ingresando con usuario: '%s'", usuario)
    context.login_page.login_completo(usuario, clave)


@then('la URL contiene "{texto}"')
def step_verificar_url(context, texto):
    logger.info("Verificando que la URL contenga: %s", texto)
    InventoryPage(context.driver)
    assert texto in context.driver.current_url, f"URL actual: {context.driver.current_url}"


@then('veo un mensaje de error que contiene "{mensaje}"')
def step_verificar_error(context, mensaje):
    logger.info("Verificando mensaje de error: %s", mensaje)
    error = context.login_page.obtener_mensaje_error()
    assert mensaje in error, f"Mensaje obtenido: '{error}'"