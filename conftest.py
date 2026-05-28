
import pytest, allure
from selenium import webdriver


@pytest.fixture()
def driver(request):
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(10)  

    yield driver

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            test_name = item.name
            screenshot = driver.save_screenshot(
            f"screenshots/{test_name}.png"
            )

            allure.attach(
                screenshot,
                name=item.name,
                attachment_type=allure.attachment_type.PNG
            )
            