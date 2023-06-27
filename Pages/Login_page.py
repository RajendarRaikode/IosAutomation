import pytest
from appium.webdriver.common.appiumby import AppiumBy
from Pages.Basepage import BasePage
from config import config

class Login_page(BasePage):

    SignIn_Heading_Check = "LoginViewControllerIdentifier_titleLabel"
    EMAILID = 'LoginViewControllerIdentifier_emailTextField'
    PASSWORD = 'LoginViewControllerIdentifier_passwordTextField'
    SHOW_PASSWORD_ICON = 'InputFiled_textFieldSecureButtonToggle'
    SIGNIN_BUTTON = 'LoginViewControllerIdentifier_signinButton'
    FORGOT_PASSWORD_TEXT = 'Forgot your password?'
    NEW_HERE_TEXT = 'New here?'
    CREATE_ACCOUNT_TEXT = 'Create an account'
    CREATE_AN_ACCOUNT_TITLE = 'titleLabel'
    TERMS_AND_CONDITIONS_TEXT = 'By accessing or using the Kidde App, you acknowledge and agree that you have read, understand, and agree to be bound by Kidde’s Terms of Service and Privacy Policy.'
    TERMS_OF_SERVICE_LINKTEXT = 'Terms of Service'
    TERMS_OF_SERVICE_TITLE = 'Terms of Service'
    PRIVACY_POLICY_LINKTEXT = 'Privacy Policy'
    PRIVACY_POLICY_TITLE = 'Privacy Policy'
    SAVE_PASSWORD_MESSAGE = 'You can view and remove saved passwords in Passwords settings.'
    SAVE_PASSWORD = 'Save Password'
    NOT_SAVE_PASSWORD = 'Not Now'
    APPRATING_AskMeLater = 'Ask Me Later'
    DASHBOARD_PAGECHECK = 'TabBarProperties.subtitle'
    INVALID_CREDENTIALS = 'Invalid email or password'

    def __init__(self, driver):
        # super.__init__(driver)
        self.driver = driver

    def SignIn_Page_Check(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.SignIn_Heading_Check)
    def get_username(self,username):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.EMAILID).send_keys(username)
    def get_password(self,password):
        self.event_send_keys(self.PASSWORD, password)

    def get_showpassword(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.SHOW_PASSWORD_ICON)
    def get_SIGNIN_click(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.SIGNIN_BUTTON)

    def get_ForgotyourPassword_linktext(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.FORGOT_PASSWORD_TEXT)

    def get_NewHere_text(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.NEW_HERE_TEXT)

    def get_CreateAccount_linktext(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.CREATE_ACCOUNT_TEXT)
    def get_terms_and_conditions_text(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.TERMS_AND_CONDITIONS_TEXT)

    def get_termsOfService_linktext(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.TERMS_OF_SERVICE_LINKTEXT)

    def get_privacyPolicy_linktext(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.PRIVACY_POLICY_LINKTEXT)

    def get_invalid_emailpassword(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.INVALID_CREDENTIALS)

    def get_savePassword_message(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.SAVE_PASSWORD_MESSAGE).text

    def get_Password_saved(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.SAVE_PASSWORD)

    def get_Without_Password_Saved(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.NOT_SAVE_PASSWORD)

    def get_apprating_later(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.APPRATING_AskMeLater)

    def get_location_access(self):
        location_permission = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Allow While Using App')
        #if location_permission.is_displayed():
        location_permission.click()
        # Allow to network
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Allow').click()
        # 'Kidde' would like to access your Home Data
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'OK').click()

    def get_notification_access(self):
        # Kidde notifications permision
        Notification_access = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Allow')
        if Notification_access.is_displayed():
            Notification_access.click()
        else:
            pass

    def forgotPassword_link_action(self):
        return self.wait_element_to_be_clickable(AppiumBy.ACCESSIBILITY_ID, self.CREATE_ACCOUNT_TEXT )
        #self.get_ForgotyourPassword_linktext().click()

    def terms_of_Service_link_action(self):
        self.get_termsOfService_linktext().click()

    def privacy_policy_link_action(self):
        self.get_privacyPolicy_linktext().click()

    def Kidde_app_login(self, username, password):
        #Page Heading check
        # assert self.SignIn_Page_Check().text == 'Sign In'
        # print("Kidde Login Page")
        #Login credentials entry
        self.driver.implicitly_wait(5)
        self.get_username(username)
        self.driver.implicitly_wait(5)
        self.get_password(password)
        self.get_SIGNIN_click().click()
        self.event_click(AppiumBy.ACCESSIBILITY_ID, self.SIGNIN_BUTTON)

    #@pytest.fixture()
    @pytest.mark.parametrize("username, password", [("rajendar.raikode@carrie.com", "Carrier@123"),
                                                    ("rajendar.raikode@carrier.com", "carrier@123"),
                                                    ("rajendar.r.com", "carrier")])
    def Kidde_Invalid_Credentials(self,username, password):
        self.Kidde_app_login(username, password)
        print("Invalid credentials, Please provide valid username and password")




    def SavePasswordCheck(self):
        if self.get_savePassword_message().text == 'You can view and remove saved passwords in Passwords settings.':
            self.get_Without_Password_Saved().click()
        else:
            self.get_Without_Password_Saved().click()

    def SignIn_to_Dashboard_Check(self):
        Dashboard_Check = self.event_get_text(AppiumBy.ACCESSIBILITY_ID, 'TabBarProperties.subtitle')
        print(Dashboard_Check)
        return Dashboard_Check



