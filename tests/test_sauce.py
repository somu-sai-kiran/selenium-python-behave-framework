from selenium.webdriver.common.by import By

def test_sauce(driver):
    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-button")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_btn.click()

    assert "inventory" in driver.current_url
    print("Login successful")

    driver.implicitly_wait(10)
