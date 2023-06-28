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

    def location_access_via_settings(self):
        try:
            #Allow to Settings for location access
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Settings').click()
            self.driver.implicitly_wait(5)
        #Kidde needs permission to use Local Network to Continue
            Access = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Allow')
            if Access.get_attribute('name') == "Allow":
                Access.click()
                #Kidde would like access your HomeData
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'OK')
                element = self.driver.find_element_by_class_name('XCUIElementTypeSwitch')
                print(element.get_attribute('value'))
                if element.get_attribute('value') == '1':
                    element.click()

                print(element.get_attribute('value'))

            else:
                print("Access denied, please allow access to location ")

        except:
            print("Mobile Location access permissions are ON")











