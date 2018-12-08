from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium import webdriver
from fixture.session import SessionHelper
# import unittest, time, re

class Application:
    def __init__(self):
        print('\nApplication_init_webdriver')
        self.driver = webdriver.Chrome('C:\\Files\\chromedriver.exe')
        self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)
        # self.base_url = "https://www.katalon.com/"
        # self.verificationErrors = []
        # self.accept_next_alert = True

    def method_new_product(self, group):
        driver = self.driver
        print('method_new_product')
        # Add New Product
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Appearance'])[1]/following::span[2]").click()
        driver.find_element_by_link_text("Add New Product").click()
        driver.find_element_by_name("name[en]").click()
        driver.find_element_by_name("name[en]").clear()
        driver.find_element_by_name("name[en]").send_keys(group.product_name)
        driver.find_element_by_name("code").click()
        driver.find_element_by_name("code").clear()
        driver.find_element_by_name("code").send_keys(group.product_code)
        driver.find_element_by_xpath("(//input[@name='categories[]'])[2]").click()
        driver.find_element_by_name("categories[]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Status'])[1]/following::label[1]").click()
        driver.find_element_by_name("save").click()


    def open_home_page(self):
        driver = self.driver
        # open home page
        driver.get("http://localhost/litecart/public_html/admin/login.php")


    def destroy(self):
        self.driver.quit()
        # self.assertEqual([], self.verificationErrors)
