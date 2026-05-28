from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


END_POINT = "https://demoqa.com/buttons"

def test_actions2(driver):
    wait = WebDriverWait(driver, 10)

    actions = ActionChains(driver)

    driver.get(END_POINT)

    assert "demosite" in driver.title, f"Page title is not matching. Expected: demosite, Got: {driver.title}"
    print(f"Page title is matching. Expected: demosite, Got: {driver.title}")

    right_click = driver.find_element(By.ID, "rightClickBtn")
    dynamic_click = driver.find_element(By.XPATH, "//button[text()='Click Me']")
    double_click = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "doubleClickBtn")
        )
    )

    actions.context_click(right_click).perform()
    actions.click(dynamic_click).perform()
    actions.double_click(double_click).perform()
    driver.save_screenshot("image2.png")
