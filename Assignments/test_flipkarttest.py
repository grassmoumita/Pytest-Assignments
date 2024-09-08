import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.HomePage import HomePage
from pageObject.ProductDetailsPage import ProductDetailsPage
from pageObject.SearchItemList import SearchItemList
from pageObject.CheckOut import CheckOut
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_endtoend(self):
        log = self.getlogger()
        wait = WebDriverWait(self.driver, 10)
        homepage = HomePage(self.driver)
        homepage.putsearchItem().send_keys("Samsung S24 128 GB")
        # homepage.putsearchItem().send_keys("Redmi 5G")
        time.sleep(5)

        try:
            homepage.searchtheitem().click()
        except Exception as e:
            print("Search button not found or could not be clicked:", e)
        time.sleep(2)
        searchitemlist = SearchItemList(self.driver)
        products = searchitemlist.getProductName()
        # print(len(products))
        if len(products)>=2:
            second_item = products[3]
            second_item.click()
            time.sleep(2)
        windowsOpened = self.driver.window_handles
        self.driver.switch_to.window(windowsOpened[1])
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,".AFOXgu").send_keys("700060")
        self.driver.find_element(By.CSS_SELECTOR,".i40dM4").click()
        success_text = self.driver.find_element(By.CLASS_NAME, "hVvnXm").text


        assert "Delivery by" in success_text


        # wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//button[text()='Add to cart']")))
        add_to_cart_button_found = False
        try:
            # add_to_cart = self.driver.find_element(By.XPATH, "//button[text()='Add to cart']")
            # add_to_cart.click()
            # print("Added to cart successfully.")
            add_to_cart_button = wait.until(
                expected_conditions.presence_of_element_located((By.XPATH,"//button[text()='Add to cart']")))
            add_to_cart_button_found = True

        except Exception as e:
            print("Standard Add to Cart button not found", e)

        if not add_to_cart_button_found:
            try:
                add_to_cart_button = wait.until(
                    expected_conditions.presence_of_element_located((By.XPATH, "//button[@class='QqFHMw vslbG+ In9uk2 JTo6b7']")))
                add_to_cart_button_found = True

            except Exception as e:
                print("SVG Add to Cart button not found")

        if add_to_cart_button_found:
            add_to_cart_button.click()
            print("Added to cart successfully.")
        else:
            print("Add to Cart button not found in either format.")



        self.driver.close()
        self.driver.switch_to.window(windowsOpened[0])
        time.sleep(2)

        homepage.returntohomepage().click()

        homepage.putsearchItem().send_keys("bajaj iron majesty")
        try:
            homepage.searchtheitem().click()
        except Exception as e:
            print("Search button not found or could not be clicked:", e)

        secondproducts = searchitemlist.getsecondProductName()
        if len(secondproducts)>=2:
            iron_second_item = secondproducts[1]
            iron_second_item.click()
            time.sleep(2)

        windowsOpened1 = self.driver.window_handles
        self.driver.switch_to.window(windowsOpened1[1])
        time.sleep(5)

        self.driver.find_element(By.CSS_SELECTOR, ".AFOXgu").send_keys("700060")
        self.driver.find_element(By.CSS_SELECTOR, ".i40dM4").click()
        second_success_text = self.driver.find_element(By.CLASS_NAME, "hVvnXm").text

        assert "Delivery by" in second_success_text

        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[text()='Add to cart']")))
        try:
            add_to_cart = self.driver.find_element(By.XPATH, "//button[text()='Add to cart']")
            add_to_cart.click()
            print("Added to cart successfully.")

        except Exception as e:
            print("Add to Cart button not found or could not be clicked:", e)

        self.driver.close()
        self.driver.switch_to.window(windowsOpened[0])
        time.sleep(2)

        homepage.returntohomepage().click()
        time.sleep(2)

        try:
            popup_cross_button = self.driver.find_element(By.CSS_SELECTOR, "._30XB9F")
            popup_cross_button.click()

        except Exception as e:
            print("No pop up is there, no need to click", e)

        time.sleep(5)
        homepage.clickoncartbutton().click()
        time.sleep(5)

        checkout = CheckOut(self.driver)

        check = self.driver.find_element(By.XPATH,"//div[@class='x9LoV+']//span[2]").text
        print("the price of iron:" + check)
        

        # sum = 0.0
        # for i in check:
        #     sum = sum + float(i.text.strip())
        #
        # print("The sum of mobile and iron is:",sum)
        #
        # totalcartprice = checkout.Total_Cart_Price().text
        #
        # print("The actual total price is:",totalcartprice)
        #
        # assert sum == totalcartprice

































