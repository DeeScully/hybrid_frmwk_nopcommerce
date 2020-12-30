class LoginPg:
    textbox_un_field_id = 'Email'
    textbox_pw_field_id = 'Password'
    btn_login_xpath = './/input[@class="button-1 login-button"]'
    lnk_logout_link_text = 'Logout'

    def __init__(self, driver):
        self.driver = driver

    def set_un(self, un):
        textbox_un_field = self.driver.find_element_by_id(self.textbox_un_field_id)
        textbox_un_field.clear()
        textbox_un_field.send_keys(un)

    def set_pw(self, pw):
        textbox_pw_field = self.driver.find_element_by_id(self.textbox_pw_field_id)
        textbox_pw_field.clear()
        textbox_pw_field.send_keys(pw)

    def click_login(self):
        btn_login = self.driver.find_element_by_xpath(self.btn_login_xpath)
        btn_login.click()

    def click_logout(self):
        lnk_logout = self.driver.find_element_by_link_text(self.lnk_logout_link_text)
        lnk_logout.click()

