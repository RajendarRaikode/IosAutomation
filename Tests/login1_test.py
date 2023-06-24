import time
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

from Pages.login1_page import Login_page1

def test_Login_Kidde_app1(init_driver):
    driver = init_driver

    login_page1 = Login_page1(driver)
    login_page1.location_access_permissions()
    login_page1.emailEntry("rajendar.raikode@carrier.com")
    print("email entered")