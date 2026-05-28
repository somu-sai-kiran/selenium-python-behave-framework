from selenium.webdriver.common.by import By


def test_google(driver):
    expected_title = "Google"

    driver.get("https://google.com")

    actual_title = driver.title
    search_box = driver.find_element(By.ID, "APjFqb")
    ai_mode = driver.find_element(By.CLASS_NAME, "lTxWLe")

    assert actual_title == expected_title, f"Title is not matching. Expected: {expected_title}, Got: {actual_title}"
    print(f"Title is matching. Expected: {expected_title}, Got: {actual_title}")

    assert search_box.is_displayed(), f"Search box is not displayed."
    print("Search box is displayed.")

    assert ai_mode.is_displayed(), f"AI Mode is not displayed."
    print("AI Mode is displayed.")