from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import login


def test_login(driver):
    login(driver)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "title"), "Products"))
    titulo = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text

    assert '/inventory.html' in driver.current_url
    assert 'products' in titulo.lower()