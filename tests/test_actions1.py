from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

end_point = "https://jqueryui.com/menu"

def test_actions1(driver):
    wait = WebDriverWait(driver, 10)

    actions = ActionChains(driver)

    driver.get(end_point)

    # validate page title
    assert "Menu" in driver.title, f"Page title is not matching. Expected: Menu, Got: {driver.title}"
    print(f"Page title is matching. Expected: Menu, Got: {driver.title}")

    iframe = driver.find_element(By.CLASS_NAME, "demo-frame")

    driver.switch_to.frame(iframe)

    electronics = driver.find_element(By.ID, "ui-id-4")
    car = driver.find_element(By.ID, "ui-id-6")
    music = driver.find_element(By.ID, "ui-id-9")


    actions.move_to_element(music).perform()

    rock = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[text()='Rock']")
        )
    )

    actions.move_to_element(rock).perform()

    alternative = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[text()='Alternative']")
        )
    )

    driver.save_screenshot("image.png")

    alternative.click()


    driver.switch_to.default_content()

    droppable = driver.find_element(By.LINK_TEXT, "Droppable")
    droppable.click()

    iframe = driver.find_element(By.CLASS_NAME, "demo-frame")
    driver.switch_to.frame(iframe)

    dragable = driver.find_element(By.ID, "draggable")
    drop = driver.find_element(By.ID, "droppable")

    actions.drag_and_drop(dragable, drop).perform()

    driver.save_screenshot("image2.png")


