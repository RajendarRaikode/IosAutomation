from appium import webdriver
import pytest
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {}


@pytest.fixture
def init_driver():
    desired_caps['platformName'] = 'iOS'
    desired_caps['platformVersion'] = '16.6'
    desired_caps['deviceName'] = 'iPhone'
    desired_caps['automationName'] = 'XCUITest'
    desired_caps['app'] = '/Users/rajendarraikode/Desktop/RemoteLync_Kidde409/RemoteLync.ipa'
    desired_caps['udid'] = '00008020-001E20DE2E68402E'
    desired_caps['bundleId'] = 'com.kidde.Kidde'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
    # yield
    # driver.close()

@pytest.fixture
def get_data():
    return [
        ("rajendar.raikode@carrie.com", "Carrier@123"),
        ("rajendar.raikode@carrier.com", "carrier@123"),
        ("rajendar.r.com", "carrier")
    ]