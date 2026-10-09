from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
class CartPage: 
    _CANTIDAD = (By.CSS_SELECTOR, "[data-test='item-quantity']")
    _NOMBRE = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    _DESCRIPCION = (By.CSS_SELECTOR, "[data-test='inventory-item-desc']")
    _PRECIO = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")

    def __init__(self, driver): 
        self.driver = driver 
        self.wait = WebDriverWait(driver, 10) 

        # Verificar que estamos en la página correcta 
        self.wait.until(EC.url_contains("cart.html")) 

    def obtener_cantidad(self):
        """Obtiene la cantidad del producto en el carrito""" 
        return self.driver.find_element(*self._CANTIDAD).text

    def obtener_nombre(self): 
        """Obtiene el nombre del producto en el carrito"""
        return self.driver.find_element(*self._NOMBRE).text

    def obtener_descripcion(self):
        """Obtiene la descripcion del producto en el carrito""" 
        return self.driver.find_element(*self._DESCRIPCION).text

    def obtener_precio(self):
        """Obtiene el precio del producto en el carrito""" 
        return self.driver.find_element(*self._PRECIO).text