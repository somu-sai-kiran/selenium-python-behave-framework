from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def select_dropdown(element, option, wait):
    element.send_keys(option)
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div[class*='option']")
        )
    )
    element.send_keys(Keys.ENTER)

def select_dropdown_child(parent, child, option, wait):
    parent.click()
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div[class*='option']")
        )
    )
    child.send_keys(option)
    child.send_keys(Keys.ENTER)

def validate_alert(wait, driver, action="accept", keys=None):
    try:
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print(alert.text)
        if keys:
            alert.send_keys(keys)
        if action == "accept":
            alert.accept()
        elif action == "dismiss":
            alert.dismiss()
        return True
    except Exception as e:
        print(e)
        return False