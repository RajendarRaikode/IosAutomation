from appium.webdriver.common.appiumby import AppiumBy
from Pages.Basepage import BasePage
from config import config

Login = {}


class Login_page(BasePage):
    # Login["emailID"] = {"Locator_type": AppiumBy.ACCESSIBILITY_ID, "email_locator": "LoginViewControllerIdentifier_emailTextField"}
    # Login["password"] = {"Locator_type": AppiumBy.ACCESSIBILITY_ID, "password_locator": "LoginViewControllerIdentifier_passwordTextField"}
    # Login["login_button"] = {"Locator_type": AppiumBy.ACCESSIBILITY_ID, "sign_in_locator": "LoginViewControllerIdentifier_signinButton"}
    # Login["Dashboard"] = {"Locator_type": AppiumBy.ACCESSIBILITY_ID, "Dashboard_locator": "TabBarProperties.subtitle"}

    EMAILID = "LoginViewControllerIdentifier_emailTextField"
    PASSWORD = "LoginViewControllerIdentifier_passwordTextField"
    SIGNIN_BUTTON = "LoginViewControllerIdentifier_signinButton"
    DASHBOARD_SIGNINCHECK = "TabBarProperties.subtitle"

    def __init__(self, driver):
        # super.__init__(driver)
        self.driver = driver

    def Kidde_app_login(self, username, password):
        # Location Access popUp handle
        location_permission = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Allow While Using App')
        if location_permission.is_displayed():
            location_permission.click()
            # Allow to network
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Allow').click()
            # 'Kidde' would like to access your Home Data
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'OK').click()

            self.event_send_keys(self.EMAILID, self.username)
            self.event_send_keys(self.PASSWORD, self.password)
            self.event_click(AppiumBy.ACCESSIBILITY_ID, self.SIGNIN_BUTTON)
        else:
            print("location access pop ups are missing")

    def SignIn_to_Dashboard_Check(self):
        return self.event_get_text(Login["Dashboard"]["Locator_type"], Login["Dashboard"]["Dashboard_locator"])

# login_page_obj = Login_page
# login_page_obj.Kidde_app_login(driver,"username", "password")


