from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    searchbar = (By.CSS_SELECTOR,".Pke_EE")
    search_button = (By.XPATH,"//button[@class='_2iLD__']")
    flipkart_image_button = (By.XPATH,"//img[@class='W5mR4e']")
    cart_button = (By.XPATH,"//a[@class='_3CowY2']")

    def putsearchItem(self):
        return self.driver.find_element(*HomePage.searchbar)

    def searchtheitem(self):
        return self.driver.find_element(*HomePage.search_button)

    def returntohomepage(self):
        return self.driver.find_element(*HomePage.flipkart_image_button)

    def clickoncartbutton(self):
        return self.driver.find_element(*HomePage.cart_button)

