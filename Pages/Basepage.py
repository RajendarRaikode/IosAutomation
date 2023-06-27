from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import config
"""This class contains all the generic methods required by all modules"""
#obj = config.TestData
#driver = obj.getDriver()
class BasePage:
    def _init_(self, driver):
        self.driver = driver
    def event_send_keys(self, by_locator,text):
        self.driver.implicitly_wait(10)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,by_locator).send_keys(text)
    def event_click(self,locator_type,by_locator):
        self.driver.implicitly_wait(10)
        self.driver.find_element(locator_type,by_locator).click()
    def wait_element_to_be_clickable(self, locator_type, by_locator):
        element_locator = self.driver.find_element(locator_type, by_locator)

        # Wait until the element is clickable
        wait = WebDriverWait(self.driver, 10)  # Maximum wait time in seconds
        element = wait.until(EC.element_to_be_clickable(element_locator))
        return element
        # Perform actions on the element

    def event_multiple_event_send_keys(self, locator_type, by_locator1, by_locator2, text):
        self.driver.implicitly_wait(60)
        print("locators")
        print(locator_type, by_locator1)
        print(locator_type,by_locator2)
        print(text)
        self.driver.find_element(locator_type, by_locator1).find_element(locator_type, by_locator2).send_keys(text)
    def event_get_text(self,locator_type,by_locator):
        self.driver.implicitly_wait(5)
        get_Text = self.driver.find_element(locator_type,by_locator).text
        return get_Text










