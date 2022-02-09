from time import sleep

from selenium.webdriver.common.by import By


def test_page_loads(driver, app_with_temp_board):
    driver.get("http://127.0.0.1:5000/")
    new_item = "Add another e2e test"

    elem = driver.find_element(By.ID, "new_item")
    elem.send_keys(new_item)
    elem.submit()
    driver.implicitly_wait(1)

    assert new_item in driver.find_element(By.CLASS_NAME, "todo-item").text
