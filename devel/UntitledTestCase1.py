# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from group import Group



class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:\\Files\\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        self.open_home_page(driver)

        self.method_login(driver, username="admin", password="admin")

        self.method_new_product(driver, Group(product_name="Product_41", product_code="Code_41"))

    def test_untitled_test_case31(self):
        driver = self.driver
        self.open_home_page(driver)

        self.method_login(driver, username="admin", password="admin")

        self.method_new_product(driver, Group(product_name="Product_31", product_code="Code_31"))

    def method_new_product(self, driver, group):
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

    def method_login(self, driver, username, password):
        # login
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Remember Me'])[1]/following::button[1]").click()

    def open_home_page(self, driver):
        # open home page
        driver.get("http://localhost/litecart/public_html/admin/login.php")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
