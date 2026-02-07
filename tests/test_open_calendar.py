import pytest
import allure
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = AppiumOptions()
options.load_capabilities({
    'platformName': "Android",
    'automationName': "UiAutomator2",
    'appium:app': "C:/Users/antio/Downloads/pnv_1.apk"
})

appium_server_url = 'http://localhost:4723'

@pytest.fixture()
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=options)
    yield android_driver
    android_driver.quit()

@allure.feature("Swipe Test")
@allure.story("Swipe to Camera")
def test_swipe(driver):
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.presence_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, "Predicted app: Package Names")
        )
    ).click()

    wait.until(
        EC.presence_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, "system apps")
        )
    ).click()

    for _ in range(10):
        with allure.step("Поиск элементов"):
            elements = driver.find_elements(
                AppiumBy.ID,
                "com.csdroid.pkg:id/tv_title"
            )

        if not elements:
            pytest.fail("Элементы не найдены")

        with allure.step("Выполнение свайпа"):
            start_x = elements[0].rect['x'] + 10
            start_y = elements[0].rect['y']
            end_x = start_x
            end_y = start_y - 600

            driver.swipe(start_x, start_y, end_x, end_y, 800)

        with allure.step("Поиск элементов после свайпа"):
            elements = driver.find_elements(
                AppiumBy.ID,
                "com.csdroid.pkg:id/tv_title"
            )
            element_names = [el.text for el in elements]

        if 'Camera' in element_names:
            break
    else:
        pytest.fail("Camera не найдена после свайпов")
