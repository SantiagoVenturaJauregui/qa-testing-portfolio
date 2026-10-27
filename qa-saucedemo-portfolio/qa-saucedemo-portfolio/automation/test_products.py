from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

BASE_URL = "https://www.saucedemo.com/"


def login(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


def test_inventory_displays_products(driver):
    login(driver)

    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0


def test_products_can_be_sorted_by_price_low_to_high(driver):
    login(driver)

    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_value("lohi")

    prices = [
        float(item.find_element(By.CLASS_NAME, "inventory_item_price").text.replace("$", ""))
        for item in driver.find_elements(By.CLASS_NAME, "inventory_item")
    ]
    assert prices == sorted(prices)


def test_products_can_be_sorted_by_name_a_to_z(driver):
    login(driver)

    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_value("az")

    names = [
        item.find_element(By.CLASS_NAME, "inventory_item_name").text
        for item in driver.find_elements(By.CLASS_NAME, "inventory_item")
    ]
    assert names == sorted(names, key=str.lower)
