from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
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










