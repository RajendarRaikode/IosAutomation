import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

def test_Kidde_app(init_driver):
    driver = init_driver
    location_permission= driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Allow While Using App')
    if location_permission.is_displayed():
        location_permission.click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Allow').click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'OK').click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'LoginViewControllerIdentifier_emailTextField').send_keys("rajendar.raikode@carrier.com")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'LoginViewControllerIdentifier_passwordTextField').send_keys("Carrier@123")
        driver.implicitly_wait(5)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'InputFiled_textFieldSecureButtonToggle').click()
        print("show password")
        time.sleep(3)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'InputFiled_textFieldSecureButtonToggle').click()
        driver.implicitly_wait(5)
        print("hide password")
    else:
        print("Your location is enabled")
