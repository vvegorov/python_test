# -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# import pytest
import unittest, time, re
from group import Group

from application import Application
print('2131231231')
print(Application())
# @pytest.fixture
# def app(request):
#     print('fixture')
#     fixture = Application()
#     request.addfinalizer(fixture.destroy())
#     return fixture
#
# def test_untitled_test_case(app):
#     print('test_untitled_test_case')
#     app.method_login(username="admin", password="admin")
class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_untitled_test_case(self):
        print('test_untitled_test_case')
        self.app.method_login(username="admin", password="admin")
        self.app.method_new_product(Group(product_name="Product_88", product_code="Code_98"))

    def test_untitled_test_case31(self):
        self.app.method_login(username="admin", password="admin")
        self.app.method_new_product(Group(product_name="Product_89", product_code="Code_99"))

    def tearDown(self):
        self.app.destroy()



