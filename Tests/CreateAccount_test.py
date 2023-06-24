import pytest
from Pages.CreateAccount_page import CreateAnAccount
from Pages.Login_page import Login_page
from config import config


def test_LoginToCreate_Page(init_driver):
    driver = init_driver
    CA = CreateAnAccount(driver)
    CA.createAnAccountClick()
def test_CreateAccountPage_Check(init_driver):
    driver = init_driver
    CA = CreateAnAccount(driver)
    CA.createAnAccountClick()
    CA.createAnAccountTitleVerify()
# def test_FirstNameHeading_Check(init_driver):
#     driver = init_driver
#     CA = CreateAnAccount(driver)
#     CA.firstNamefieldHeadingCheck()
# def test_FirstNameTextEntry(init_driver):
#     driver = init_driver
#     CA = CreateAnAccount(driver)
#     CA.FirstNameFieldEntry("Appium")
def test_EmailHeadingCheck(init_driver):
    driver = init_driver
    CA = CreateAnAccount(driver)
    CA.getEmailHeading()
def test_Emailentry(init_driver):
    driver = init_driver
    CA = CreateAnAccount(driver)
    CA.EmailEntry("rajendar.raikode@carrier.com")


