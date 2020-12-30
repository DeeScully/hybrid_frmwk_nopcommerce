import pytest
from selenium import webdriver
from page_objects.login_pg import LoginPg
from selenium.webdriver.common.keys import Keys
from datetime import date
from utils.read_properties import ReadConfig
from utils.custom_logger import LogGen

#run tests by using command pytest -v -n=2 --html=reports\report.html
class Test001Login:
    base_url = ReadConfig.get_app_url()
    un = ReadConfig.get_username()
    pw = ReadConfig.get_password()
    today = date.today().strftime("%Y%m%d")
    logger = LogGen.log_gen()

    @pytest.mark.regression
    def test_homepg_title(self, setup):
        self.logger.info('***Test001Login***') #create own log msgs
        self.logger.info('testing test_homepg_title...')
        self.driver = setup
        self.driver.get(self.base_url)
        actual_homepg_title = self.driver.title
        expected_homepg_title = 'Your store. Login'
        if actual_homepg_title != expected_homepg_title:
            self.driver.save_screenshot(f'.\\screengrabs\\{self.today}test_homepg_title.png')
            self.driver.quit()
            self.logger.error('test_homepg_title test FAILED')
            assert False

        self.driver.quit()
        assert True
        self.logger.info('test_homepg_title test passed')

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_good_creds(self, setup):
        self.logger.info('test_login_good_creds...')
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_pg = LoginPg(self.driver)
        self.login_pg.set_un(self.un)
        self.login_pg.set_pw(self.pw)
        self.login_pg.click_login()
        actual_dashboardpg_title = self.driver.title
        expected_dashboardpg_title = 'Dashboard / nopCommerce administration'
        if actual_dashboardpg_title != expected_dashboardpg_title:
            self.driver.save_screenshot(f'.//screengrabs//{self.today}test_login_good_creds.png')
            self.driver.quit()
            self.logger.error('test_login_good_creds test FAILED')
            assert False

        self.driver.quit()
        assert True
        self.logger.info('test_login_good_creds test passed')