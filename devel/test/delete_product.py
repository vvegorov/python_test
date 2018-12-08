# -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# import pytest
import unittest
from model.group import Group

from fixture.application import Application
print('START!!!')
# print(Application())
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
        self.test = ''

    def test_untitled_test_case_delete(self):
        print('test_untitled_test_case_delete_START')
        self.app.session.method_login(username="admin", password="admin")
        # self.app.product.create(Group(product_name="Product_110", product_code="Code_110"))
        self.app.product.delete()
        self.test = 'test_untitled_test_case_delete'

    # def test_untitled_test_case31(self):
    #     print('test_untitled_test_case31_START')
    #     self.app.session.method_login(username="admin", password="admin")
    #     self.app.product.create(Group(product_name="Product_104", product_code="Code_104"))
    #     self.test = 'test_untitled_test_case31'

    def tearDown(self):
        print(self.test + '_END')
        self.app.destroy()



