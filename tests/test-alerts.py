from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

driver.get("https://demoqa.com/alerts")

assert "demosite" in driver.title, f"Title mismatch. Expected:demosite, Actual:{driver.title}"
print(f"Title is matching. Expected:demosite, Actual:{driver.title}")

alert_btn = driver.find_element(By.ID, "alertButton")
timer_alert_btn = driver.find_element(By.ID, "timerAlertButton")
confirmation_btn = driver.find_element(By.ID, "confirmButton")
prompt_btn = driver.find_element(By.ID, "promtButton")

assert alert_btn and timer_alert_btn and confirmation_btn and prompt_btn, "All Buttons are not identifiable"
print("All buttons are identifiable") 

alert_btn.click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

timer_alert_btn.click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

confirmation_btn.click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.dismiss()
wait.until(EC.visibility_of_element_located((By.ID, "confirmResult")))
print(driver.find_element(By.ID, "confirmResult").text)

prompt_btn.click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.send_keys("Hello Guruji!!!!")
alert.accept()
wait.until(EC.visibility_of_element_located((By.ID, "promptResult")))
print(driver.find_element(By.ID, "promptResult").text)

driver.quit()