from selenium.webdriver.common.by import By

BASE_URL = "https://www.saucedemo.com/"


def login(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


def test_checkout_with_valid_information_completes_order(driver):
    login(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("1000")
    driver.find_element(By.ID, "continue").click()

    assert "/checkout-step-two.html" in driver.current_url
    driver.find_element(By.ID, "finish").click()

    assert "/checkout-complete.html" in driver.current_url
    confirmation = driver.find_element(By.CLASS_NAME, "complete-header")
    assert "thank you for your order" in confirmation.text.lower()


def test_checkout_requires_first_name(driver):
    login(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("1000")
    driver.find_element(By.ID, "continue").click()

    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert error.is_displayed()
    assert "first name is required" in error.text.lower()
