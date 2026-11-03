import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pathlib
import pytest_html

target = pathlib.Path('reports/screens')
target.mkdir(parents=True, exist_ok=True)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == 'call' and report.failed: 
        driver = item.funcargs.get('driver')
        if driver: 
            file_name = target / f"{item.name}.png" 
            driver.save_screenshot(str(file_name)) 

            extras = getattr(report, 'extras', [])
            extras.append(pytest_html.extras.image(driver.get_screenshot_as_base64(), 'screenshot'))
            report.extras = extras

@pytest.fixture
def driver():
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()