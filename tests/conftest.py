import pytest
from appium.options.android import UiAutomator2Options
from helper.get_device_android import get_connected_device_capabilities
from helper.init_appium_session import AppiumDriver


@pytest.fixture
def start_session():
    """
    start session appium
    :return:
    """
    capabilities = dict(
        platformName='Android',
        automationName='UiAutomator2',
        deviceName='Pixel 3a API 31',
        appPackage='org.wikipedia',
        platformVersion='12.0',
        appActivity='.main.MainActivity'
    )

    connected_device_capabilities = get_connected_device_capabilities()

    if connected_device_capabilities:
        capabilities.update(connected_device_capabilities)

    appium_driver = AppiumDriver()
    appium_driver.create_driver(url='http://127.0.0.1:4723/wd/hub',
                                capabilities=UiAutomator2Options().load_capabilities(caps=capabilities))
    yield appium_driver
    appium_driver.quit_driver()

