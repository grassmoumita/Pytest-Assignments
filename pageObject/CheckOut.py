from selenium.webdriver.common.by import By

class CheckOut:

    def __init__(self,driver):
        self.driver = driver

    itemspriceincart = (By.XPATH,"//div[@class='x9LoV+']/span[@class='LAlF6k re6bBo']")
    totalamount = (By.XPATH,"//div[@class='PWd9A7 xvz6eC']/div[@class='_1Y9Lgu']/span")

    def Cart_Items_Price(self):
        return self.driver.find_elements(*CheckOut.itemspriceincart)

    def Total_Cart_Price(self):
        return self.driver.find_element(*CheckOut.itemspriceincart)
