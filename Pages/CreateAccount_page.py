import time
from appium.webdriver.common.appiumby import AppiumBy
from Pages.Basepage import BasePage

class CreateAnAccount(BasePage):

    def __init__(self,driver):
        self.driver = driver

    CREATEACCOUNT_CLICK_XPATH = "//*[(@text = 'Create an account')]"
    CREATEANACCOUNT_TITLE_ID = "com.kidde.android.monitor1:id/get_started_text1"
    GOBACK_ICON_ID = "com.kidde.android.monitor1:id/back_icon"
    #FIRSTNAME_HEADING_XPATH = ""
    #FIRSTNAME_TEXTFIELD_ID = "com.kidde.android.monitor1:id/first_name"
    #LASTNAME_HEADING = ""
    #LASTNAME_TEXTFIELD_ID = ""
    EMAIL_HEADING_XPATH = "//*[(@text = 'Email')]"
    EMAIL_TEXTFIELD_XPATH = "//*[(@text = 'name@kidde.com')]"
    #PASSWORD_HEADING_
    #PASSWORD_TEXTFIELD_ID = ""

    def getCreateAccountLink(self):
        linktext = self.driver.find_element(AppiumBy.XPATH, self.CREATEACCOUNT_CLICK_XPATH)
        return linktext
    def getCreateAccountpageTitle(self):
        return self.driver.find_element(AppiumBy.ID, self.CREATEANACCOUNT_TITLE_ID)
    # def getFirstNameHeading(self):
    #     return self.driver.find_element(AppiumBy.ID,self.FIRSTNAME_HEADING_XPATH)
    # def getFirstNameTextEnter(self):
    #     return self.driver.find_element(AppiumBy.ID, self.FIRSTNAME_TEXTFIELD_ID)
    #def getLastNameHeading(self):
        #return self.driver.find_element(AppiumBy.ID,self.LASTNAME_HEADING)
    #def getLastNameTextField(self):
        #return self.driver.find_element(AppiumBy.ID,self.LASTNAME_TEXTFIELD_ID)
    def getEmailHeading(self):
        return self.driver.find_element(AppiumBy.XPATH, self.EMAIL_HEADING_XPATH)
    def getEmailText(self):
        return self.driver.find_element(AppiumBy.XPATH, self.EMAIL_TEXTFIELD_XPATH)
    #def getPasswordHeading(self):
        #return self.driver.find_element(AppiumBy.)



    def createAnAccountClick(self):
        self.getCreateAccountLink().click()
        time.sleep(2)

    def createAnAccountTitleVerify(self):
        CreateTitle = self.getCreateAccountpageTitle().text
        assert 'Create an account' in CreateTitle
        print("Enter the details to create your account")
    def firstNamefieldHeadingCheck(self):
        firstnameHeading = self.getFirstNameHeading().text
        assert 'Firstname' in firstnameHeading

    def FirstNameFieldEntry(self, firstname):
        self.getFirstNameTextEnter().send_keys(firstname)
        print(firstname)

    # def LastNameFieldEntry(self,lastname):
    #     self.getLastNameTextField().sendKeys(lastname)
    #     print(lastname)

    def emailHeadingVerify(self):
        emailheading = self.getEmailHeading().text
        assert 'Email' in emailheading


    def EmailEntry(self,email):
        self.getEmailText().send_keys(email)
        print(email)

    #def PasswordEntry(self,password):
        #self.getPasswordEntry



