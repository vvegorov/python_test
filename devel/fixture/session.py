class SessionHelper:

    def __init__(self,app):
        self.app = app


    def method_login(self, username, password):
        driver = self.app.driver
        self.app.open_home_page()
        print('method_login')
        # login
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Remember Me'])[1]/following::button[1]").click()
