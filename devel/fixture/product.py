from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class ProductHelper:

    def __init__(self,app):
        self.app = app
        self.accept_next_alert = True

    def create(self, group):
        driver = self.app.driver
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


    def delete(self):
        driver = self.app.driver
        print('method_delete')
        # Add New Product
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Appearance'])[1]/following::span[2]").click()
        driver.find_element_by_link_text("NewCategory234").click()
        driver.find_element_by_name("products[79]").click()
        driver.find_element_by_name("delete").click()
        driver.switch_to_alert().accept()
        # WebDriverWait(driver, 5).until(EC.alert_is_present).accept()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Catalog'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Appearance'])[1]/preceding::i[4]").click()
