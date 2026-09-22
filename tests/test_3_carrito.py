from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import login

def test_carrito(driver):
    login(driver)
    # lista de productos 
    productos = driver.find_elements(By.CSS_SELECTOR, "div.inventory_item")
    #  nombre de 1er producto   
    nombre = productos[0].find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text
    # precio del 1er producto     
    precio = productos[0].find_element(By.CSS_SELECTOR, "[data-test='inventory-item-price']").text
    productos[0].find_element(By.TAG_NAME, "button").click()
    # chequear incremento del carrito (espera explícita: tarda en actualizar)
    wait = WebDriverWait(driver, 10)
    badge = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='shopping-cart-badge']"))
    )
    assert badge.text == "1"

    # clickear el carrito data-test="shopping-cart-link"
    driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']").click()

    # esperar a que cargue la página del carrito 
    cantidad = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='item-quantity']"))
    )
    cantidad = cantidad.text
    assert cantidad == "1"
    # checkear titulo data-test="inventory-item-name"
    titulo_carrito = driver.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text
    assert titulo_carrito == nombre
    # checkear descripcion data-test="inventory-item-desc"
    descripcion = driver.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-desc']").text
    assert descripcion != ""
    # checkear precio data-test="inventory-item-price"
    precio_carrito = driver.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-price']").text
    assert precio_carrito == precio



  
