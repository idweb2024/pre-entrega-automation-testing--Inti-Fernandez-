from selenium.webdriver.common.by import By


def login(driver, usuario="standard_user", contrasenia="secret_sauce"):
    """Completa el formulario de login de SauceDemo con las credenciales dadas."""
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(contrasenia)
    driver.find_element(By.ID, "login-button").click()