from selenium.webdriver.common.by import By

class ProductDetailsPage:
    def __init__(self,driver):
        self.driver = driver

    enterPincode = (By.CSS_SELECTOR, ".AFOXgu")
    checkpincode = (By.CSS_SELECTOR,".i40dM4")
    pincodecheckstatus = (By.CSS_SELECTOR,".hVvnXm")

    def EnterPincode(self):
        return self.driver.find_element(*ProductDetailsPage.enterPincode)

    def CheckPincode(self):
        return self.driver.find_element(*ProductDetailsPage.checkpincode)

    def PincodeStatusCheck(self):
        return self.driver.find_element(*ProductDetailsPage.pincodecheckstatus)
