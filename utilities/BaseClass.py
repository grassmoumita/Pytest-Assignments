import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        # logger = logging.getLogger(__name__)  # this will log everything, if not mentioned __name__, i will print root
        logger = logging.getLogger(loggerName)     #this will print the exact calling function name
        fileHandler = logging.FileHandler('logfile.log')  # in this file the log will create
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger


    # def verifylinkpresence(self,text):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

