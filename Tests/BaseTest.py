import pytest

@pytest.mark.usefixtures("init_driver")
class BaseTest:
   # driver = init_driver
   print("this came from init_driver")
   pass
