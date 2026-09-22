from selenium.webdriver.common.by import By
from utils.helpers import login

def test_catalogo(driver):
    login(driver)
    titulo = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert titulo == "Products"

    productos = driver.find_elements(By.CSS_SELECTOR, "div.inventory_item")
    assert len(productos) > 0

    nombre = productos[0].find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text
    assert nombre != ""
    print("Primer producto →", nombre)

    precio = productos[0].find_element(By.CSS_SELECTOR, "[data-test='inventory-item-price']").text
    assert precio != ""
    print("Precio →", precio)






