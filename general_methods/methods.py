import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from helper.init_appium_session import AppiumDriver


def scroll_test(direction, duration, count_scroll=5):
    driver = AppiumDriver().driver
    size = driver.get_window_size()
    start_y = size['height'] * 0.8
    end_y = size['height'] * 0.2
    try:
        for _ in range(count_scroll):
            if direction.lower() == 'вниз':
                driver.swipe(start_x=size['width'] // 2, start_y=start_y, end_x=size['width'] // 2,
                                  end_y=end_y, duration=duration)
            elif direction.lower() == 'вверх':
                driver.swipe(start_x=size['width'] // 2, start_y=end_y, end_x=size['width'] // 2,
                                  end_y=start_y, duration=duration)
            else:
                raise ValueError("Неверное направление. Используйте 'вниз' или 'вверх'.")
    except Exception as e:
        raise e


def tap(locator):
    driver = AppiumDriver().driver
    element = driver.find_element(By.ID, locator)
    element.click()


def wait_for_element_by_locator(locator, timeout=10):
    driver = AppiumDriver().driver
    end_time = time.time() + timeout
    while time.time() < end_time:
        try:
            element = driver.find_element(By.ID, locator)
            if element:
                return element
        except NoSuchElementException:
            pass
        time.sleep(1)
    raise TimeoutException(f"Элемент с локатором '{locator}' не был найден за отведенное время")
