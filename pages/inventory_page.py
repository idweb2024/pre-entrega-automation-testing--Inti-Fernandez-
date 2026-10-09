from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    _TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    _ITEM_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    _ITEM_PRICES = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    _ADD_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='add-to-cart']")
    _CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    _CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.wait.until(EC.url_contains("inventory.html"))

    def obtener_titulo(self):
        """Obtiene el título de la página de inventario."""
        return self.driver.find_element(*self._TITLE).text

    def obtener_nombres(self):
        """Obtiene los nombres (texto) de los productos disponibles."""
        elementos = self.driver.find_elements(*self._ITEM_NAMES)
        return [elemento.text for elemento in elementos]

    def obtener_precios(self):
        """Obtiene los precios (texto) de los productos disponibles."""
        elementos = self.driver.find_elements(*self._ITEM_PRICES)
        return [elemento.text for elemento in elementos]

    def agregar_primer_producto(self):
        """Añade el primer producto disponible al carrito."""
        primer_boton = self.driver.find_elements(*self._ADD_BUTTONS)[0]
        primer_boton.click()
        return self

    def obtener_contador_carrito(self):
        """Espera a que el badge sea visible y devuelve su valor como número."""
        badge = self.wait.until(EC.visibility_of_element_located(self._CART_BADGE))
        return int(badge.text)

    def ir_al_carrito(self):
        """Navega a la página del carrito."""
        self.driver.find_element(*self._CART_LINK).click()
        # Importación lazy para evitar dependencias circulares
        from pages.cart_page import CartPage
        return CartPage(self.driver)

    def hacer_logout(self):
        """Cierra la sesión del usuario."""
        self.driver.find_element(*self._MENU_BUTTON).click()
        logout_link = self.wait.until(EC.element_to_be_clickable(self._LOGOUT_LINK))
        logout_link.click()
        from pages.login_page import LoginPage
        return LoginPage(self.driver)