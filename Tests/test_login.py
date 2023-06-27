import pytest

from Pages.Login_page import Login_page
from config import config
import Tests.conftest as tc
import json
testdata_obj = config.TestData

def test_SignIn_Page_Check(init_driver):
    driver = init_driver
    login_page = Login_page(driver)
    login_page.get_location_access()
    driver.implicitly_wait(5)
    assert login_page.SignIn_Page_Check().text == "Sign In"
    print("You are in Kidde SignIn Page, Please enter your credentials")

def test_ShowPassword_Icon_check(init_driver):
    driver = init_driver
    login_page = Login_page(driver)
    login_page.get_location_access()
    driver.implicitly_wait(5)
    assert login_page.get_showpassword().is_displayed()

def test_ForgotPasswordText_check(init_driver):
    driver = init_driver
    login_page = Login_page(driver)
    login_page.get_location_access()
    driver.implicitly_wait(5)
    assert login_page.get_ForgotyourPassword_linktext().text == "Forgot your password?"
    login_page.forgotPassword_link_action()
def test_NewHere_Text_check(init_driver):
    driver = init_driver
    login_page = Login_page(driver)
    login_page.get_location_access()
    driver.implicitly_wait(5)
    assert login_page.get_NewHere_text().text == "New here?"

def test_CreateanAccount_Text_check(init_driver):
    driver = init_driver
    login_page = Login_page(driver)
    login_page.get_location_access()
    driver.implicitly_wait(5)
    assert login_page.get_CreateAccount_linktext().text == "Create an account"

def test_Terms_Conditions_Text_check(init_driver):
    driver = init_driver
    login_page = Login_page(driver)
    login_page.get_location_access()
    driver.implicitly_wait(5)
    assert login_page.get_terms_and_conditions_text().text == "By accessing or using the Kidde App, you acknowledge and agree that you have read, understand, and agree to be bound by Kidde’s Terms of Service and Privacy Policy."

def test_TermsOfService_link_check(init_driver):
    driver = init_driver
    login_page = Login_page(driver)
    login_page.get_location_access()
    driver.implicitly_wait(5)
    #login_page.terms_of_Service_link_action()
    login_page.get_termsOfService_linktext().click()
def test_Login_Kidde_app(init_driver):
    driver = init_driver
    login_page = Login_page(driver)
    username = testdata_obj.username
    password = testdata_obj.password
    test_SignIn_Page_Check(init_driver)
    login_page.Kidde_app_login(username, password)
    login_page.get_notification_access()
    #login_page.SavePasswordCheck()
    #login_page.get_apprating_later().click()
    assert 'Good' in login_page.SignIn_to_Dashboard_Check()
    driver.implicitly_wait(5)

def test_Kidde_unregistered_username(init_driver):
    driver = init_driver
    login_page = Login_page(driver)
    username = testdata_obj.Unregistered_username
    password = testdata_obj.password
    login_page.get_location_access()
    login_page.Kidde_app_login(username, password)
    driver.implicitly_wait(5)
    assert login_page.get_invalid_emailpassword().text == "Invalid email or password"


def test_Kidde_Invalid_username(init_driver):
    driver = init_driver
    login_page = Login_page(driver)
    username = testdata_obj.Invalid_username
    password = testdata_obj.password
    login_page.get_location_access()
    login_page.Kidde_app_login(username, password)
    driver.implicitly_wait(5)
    assert login_page.get_invalid_emailpassword().text == "Invalid email or password"


def test_Kidde_Invalid_password(init_driver):
    driver = init_driver
    login_page = Login_page(driver)
    username = testdata_obj.username
    password = testdata_obj.Invalid_password
    login_page.get_location_access()
    login_page.Kidde_app_login(username, password)
    driver.implicitly_wait(5)
    assert login_page.get_invalid_emailpassword().text == "Invalid email or password"


def test_Kidde_Invalid_username_password(init_driver):
    driver = init_driver
    login_page = Login_page(driver)
    username = testdata_obj.Unregistered_username
    password = testdata_obj.Invalid_password
    login_page.get_location_access()
    login_page.Kidde_app_login(username, password)
    driver.implicitly_wait(5)
    assert login_page.get_invalid_emailpassword().text == "Invalid email or password"


def test_empty_Username(init_driver):
    driver = init_driver
    login_page = Login_page(driver)
    username = testdata_obj.Null_username
    password = testdata_obj.password
    login_page.get_location_access()
    login_page.Kidde_app_login(username, password)
    driver.implicitly_wait(5)
    assert login_page.get_SIGNIN_click().isnotclickable()





# def test_Login_Kidde_app(init_driver):
#     driver = init_driver
#     login_page = Login_page(driver)
#     url = cloudDataObj.cloud_login_url
#     headers = cloudDataObj.headers
#    user_email = cloudDataObj.email
#     user_password = cloudDataObj.password
#     user_timezone = cloudDataObj.timezone
#     user_language = cloudDataObj.language
#     payload = json.dumps({"email":user_email,
#                           "password":user_password,
#                           "timezone":user_timezone,
#                           "language":user_language
#                           })
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#     assert response.status_code == 200
    #checking_text = login_page.Kidde_app_login(testdata_obj.username, testdata_obj.password)
    #assert checking_text == "ADD A DEVICE"






