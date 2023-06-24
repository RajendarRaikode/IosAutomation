from appium.webdriver.common.appiumby import AppiumBy
from Pages.Basepage import BasePage
from config import config

Login = {}

class Login_page1(BasePage):

    EMAIL = 'LoginViewControllerIdentifier_emailTextField'
    EMAIL_XPATH = '//XCUIElementTypeTextField[@name="LoginViewControllerIdentifier_emailTextField"]'
    PASSWORD = 'LoginViewControllerIdentifier_passwordTextField'
    SIGNIN_BUTTON = 'LoginViewControllerIdentifier_signinButton'
    DASHBOARD_SIGNINCHECK = 'TabBarProperties.subtitle'

    def __init__(self, driver):
        # super.__init__(driver)
        self.driver = driver

    def location_access_permissions(self):
        location_permission = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Allow While Using App')
        if location_permission.is_displayed():
            location_permission.click()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Allow').click()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'OK').click()
    def get_username(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.EMAIL)
    def emailEntry(self, username):
        self.get_username().send_keys(username)