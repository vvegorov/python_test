from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.product import ProductHelper
# import unittest, time, re

class Application:
    def __init__(self):
        print('\nApplication_init_webdriver')
        self.driver = webdriver.Chrome('C:\\Files\\chromedriver.exe')
        self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.product = ProductHelper(self)
        # self.base_url = "https://www.katalon.com/"
        # self.verificationErrors = []
        # self.accept_next_alert = True

    def open_home_page(self):
        driver = self.driver
        # open home page
        driver.get("http://localhost/litecart/public_html/admin/login.php")


    def destroy(self):
        self.driver.quit()
        # self.assertEqual([], self.verificationErrors)
