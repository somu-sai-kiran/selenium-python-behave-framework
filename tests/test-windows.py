from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

driver.get("https://the-internet.herokuapp.com/windows")

main_window = driver.current_window_handle

print("Main Window:", main_window)

assert "The Internet" in driver.title, f"Page title is not matching. Expected: The Internet, Got: {driver.title}"
print(f"Page title is matching. Expected: The Internet, Got: {driver.title}")

heading = driver.find_element(By.XPATH, "//div[@ID='content']/div/h3")

assert "Opening a new window" in heading.text, f"Page heading is not matching. Expected: Opening a new window, Got: {heading.text}"
print(f"Page heading is matching. Expected: Opening a new window, Got: {heading.text}")

btn = driver.find_element(By.XPATH, "//div[@ID='content']/div/a")
# print(btn.text)

btn.click()

wait.until(lambda d: len(d.window_handles) == 2)

all_windows = driver.window_handles

for window in all_windows:
    if window != main_window:
        driver.switch_to.window(window)

print("Switched to new window")

assert "New Window" in driver.title, f"Page title is not matching. Expected: New Window, Got: {driver.title}"
print(f"Page title is matching. Expected: New Window, Got: {driver.title}")

heading = driver.find_element(By.XPATH, "//div[@CLASS='example']/h3")

assert "New Window" in heading.text, f"Page heading is not matching. Expected: New Window, Got: {heading.text}"
print(f"Page heading is matching. Expected: New Window, Got: {heading.text}")

driver.close()

driver.switch_to.window(main_window)

driver.quit()