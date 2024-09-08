from selenium.webdriver.common.by import By

class SearchItemList:
    def __init__(self,driver):
        self.driver = driver

    mobile_product = (By.XPATH, "//a[@class='CGtC98']")
    iron_product = (By.XPATH,"//a[@class='wjcEIp']")

    def getProductName(self):
        return self.driver.find_elements(*SearchItemList.mobile_product)

    def getsecondProductName(self):
        return self.driver.find_elements(*SearchItemList.iron_product)


