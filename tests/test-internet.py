from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

# Wait until start button clickable
start = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[@id='start']/button")
    )
)

print("Element clickable")

start.click()

print("Button clicked")

# Wait until finish text visible
finish = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "finish")
    )
)

assert finish.is_displayed(), "Finish text not displayed"

print("Finish text found bro test case passed")

driver.save_screenshot(
    r"C:\Users\saiki\Documents\Git-Repos\selenium-python-behave-framework\screenshots\test-internet.png"
)

driver.quit()