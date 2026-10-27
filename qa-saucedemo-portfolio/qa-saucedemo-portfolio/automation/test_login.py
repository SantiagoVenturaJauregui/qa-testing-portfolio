from selenium.webdriver.common.by import By

BASE_URL = "https://www.saucedemo.com/"


def test_login_with_valid_credentials(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "/inventory.html" in driver.current_url
    assert driver.find_elements(By.CLASS_NAME, "inventory_item")


def test_login_with_invalid_password_shows_error(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert error.is_displayed()
    assert "do not match" in error.text.lower()


def test_login_with_empty_fields_shows_error(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "login-button").click()

    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert error.is_displayed()
    assert "username is required" in error.text.lower()
