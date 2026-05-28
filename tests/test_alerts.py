import allure
from utils.helpers import validate_alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

END_POINT = "https://demoqa.com/alerts"


@allure.title("Validate Alerts Page Title")
@allure.description("Verify whether the Alerts page title loads correctly.")
def test_title(driver):

    driver.get(END_POINT)

    assert "demosite" in driver.title, \
        f"Title mismatch. Expected:demosite, Actual:{driver.title}"

    print(f"Title is matching. Expected:demosite, Actual:{driver.title}")


@allure.title("Validate Simple Alert")
@allure.description("Verify simple JavaScript alert handling using accept action.")
def test_alert_btn(driver):

    driver.get(END_POINT)

    wait = WebDriverWait(driver, 10)

    alert_btn = driver.find_element(By.ID, "alertButton")

    alert_btn.click()

    assert validate_alert(wait, driver), \
        f"Alert not found"

    print("Validated Alert Button")


@allure.title("Validate Timer Alert")
@allure.description("Verify delayed alert handling using explicit wait and dismiss action.")
def test_timer_btn(driver):

    driver.get(END_POINT)

    wait = WebDriverWait(driver, 10)

    timer_alert_btn = driver.find_element(By.ID, "timerAlertButton")

    timer_alert_btn.click()

    assert validate_alert(wait, driver, "dismiss"), \
        f"Alert not found"

    print("Validated Timer Alert Button")


@allure.title("Validate Confirmation Alert")
@allure.description("Verify confirmation alert handling and success message validation.")
def test_confirmation_btn(driver):

    driver.get(END_POINT)

    wait = WebDriverWait(driver, 10)

    confirmation_btn = driver.find_element(By.ID, "confirmButton")

    confirmation_btn.click()

    assert validate_alert(wait, driver), \
        f"Alert not found"

    print("Validated Confirmation Alert")

    confirmation_btn.click()

    assert validate_alert(wait, driver), \
        f"Alert not found"

    print("Validated Confirmation Alert")

    assert wait.until(
        EC.visibility_of_element_located((By.ID, "confirmResult"))
    ), f"Success text is not visible"

    print(driver.find_element(By.ID, "confirmResult").text)


@allure.title("Validate Prompt Alert")
@allure.description("Verify prompt alert handling with text input and success message validation.")
def test_prompt_btn(driver):

    driver.get(END_POINT)

    wait = WebDriverWait(driver, 10)

    prompt_btn = driver.find_element(By.ID, "promtButton")

    prompt_btn.click()

    assert validate_alert(
        wait,
        driver,
        keys="Hello Guruji"
    ), f"Alert not found"

    print("Validated Prompt Alert")

    wait.until(
        EC.visibility_of_element_located((By.ID, "promptResult"))
    ), f"Success text is not visible"

    print(driver.find_element(By.ID, "promptResult").text)