from selenium.webdriver.common.by import By

BASE_URL = "https://www.saucedemo.com/"
BACKPACK_ADD_BUTTON = "add-to-cart-sauce-labs-backpack"
BACKPACK_REMOVE_BUTTON = "remove-sauce-labs-backpack"


def login(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


def test_add_product_to_cart(driver):
    login(driver)
    driver.find_element(By.ID, BACKPACK_ADD_BUTTON).click()

    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    product_names = [
        element.text
        for element in driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    ]
    assert "Sauce Labs Backpack" in product_names


def test_remove_product_from_cart_on_inventory_page(driver):
    login(driver)
    driver.find_element(By.ID, BACKPACK_ADD_BUTTON).click()
    driver.find_element(By.ID, BACKPACK_REMOVE_BUTTON).click()

    assert not driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")


def test_cart_page_shows_added_product(driver):
    login(driver)
    driver.find_element(By.ID, BACKPACK_ADD_BUTTON).click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    names = [
        element.text
        for element in driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    ]
    assert names == ["Sauce Labs Backpack"]
