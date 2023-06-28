import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class TestData:
    username = "rajendar.raikode@carrier.com"
    password = "Carrier@123"
    Unregistered_username = "ioscloud755@gmail.com"
    Invalid_username = "rajendar.raikode@carri.com"
    Invalid_password = "carrier"
    Null_username = ""
    Null_password = ""

class CloudTestData:
    cloud_login_url = "https://api.kidde-remotelync.com/api/v4/auth/login"
    headers = {
        'Content-Type': 'text/plain'
    }
    email = "rajendar.raikode@carrier.com"
    password ="Carrier@123"
    timezone = "Asia/Calcutta"
    language = "en"





