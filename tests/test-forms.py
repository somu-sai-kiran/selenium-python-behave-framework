from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

end_point = "https://demoqa.com/automation-practice-form"

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get(end_point)

def select_dropdown(element, option):
    element.send_keys(option)
    time.sleep(2)
    element.send_keys(Keys.ENTER)

def select_dropdown_child(parent, child, option):
    parent.click()
    time.sleep(2)
    child.send_keys(option)
    child.send_keys(Keys.ENTER)

# Validate page title
assert "demosite" in driver.title, f"Title is not matching. Expected: demosite, Got: {driver.title}"
print(f"Title is matching. Expected: demosite, Got: {driver.title}")

first_name = driver.find_element(By.ID, "firstName")
last_name = driver.find_element(By.ID, "lastName")
email = driver.find_element(By.ID, "userEmail")
male_label = driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']")
mobile_number = driver.find_element(By.ID, "userNumber")
dob = driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']")
subjects = driver.find_element(By.ID, "subjectsInput")
sports = driver.find_element(By.ID, "hobbies-checkbox-1")
picture = driver.find_element(By.ID, "uploadPicture")
current_address = driver.find_element(By.ID, "currentAddress")
state = driver.find_element(By.XPATH, "//div[@id='state']")
state_input = driver.find_element(By.ID, "react-select-3-input")
city = driver.find_element(By.XPATH, "//div[@id='city']")
city_input = driver.find_element(By.ID, "react-select-4-input")
submit = driver.find_element(By.ID, "submit")

first_name.send_keys("Saikiran")
last_name.send_keys("Somu")
email.send_keys("saikiransomu@gmail.com")
mobile_number.send_keys("9874561230")
male_label.click()
select_dropdown(subjects, "History")
select_dropdown(subjects, "Hindi")
sports.click()
picture.send_keys(r"c:\Users\saiki\Pictures\Camera Roll\P1050069.JPG")
current_address.send_keys("Vijayawada")
select_dropdown_child(state, state_input, "NCR")
select_dropdown_child(city, city_input, "Delhi")
dob.send_keys("24 May 2026")

submit.click()

close = driver.find_element(By.ID, "closeLargeModal")
driver.implicitly_wait(10)
driver.save_screenshot(r"C:\Users\saiki\Documents\Git-Repos\selenium-python-behave-framework\screenshots\form_submission_test_evidence.png")

# Validate form submission
assert close.is_displayed(), "Form submission failed"
print("Form submitted successfully")

driver.quit()
