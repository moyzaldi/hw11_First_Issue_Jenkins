import allure
from selene import browser
import allure
import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    with allure.step("Параметры браузера"):
        options = Options()
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "126.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }

        options.capabilities.update(selenoid_capabilities)
        driver = webdriver.Remote(
            command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
            options=options)

        browser.config.driver = driver
        browser.config.window_height = 1080
        browser.config.window_width = 1920
        browser.config.base_url = 'https://demoqa.com'
        browser.config.timeout = 20

        yield
        browser.quit()