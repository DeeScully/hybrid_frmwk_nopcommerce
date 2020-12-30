import pytest

from page_objects.login_pg import LoginPg
from page_objects.add_cust_pg import AddCust
from page_objects.search_cust_pg import SearchCust
from datetime import date
from utils.read_properties import ReadConfig
from utils.custom_logger import LogGen
import string
import random
import time
'''run test pytest -v --html=reports\insert_date\report.html test_cases\test_search_customer_by_name.py'''

class Test005SearchCustName:
    base_url = ReadConfig.get_app_url()
    un = ReadConfig.get_username()
    pw = ReadConfig.get_password()
    today = date.today().strftime("%Y%m%d")
    logger = LogGen.log_gen()

    @pytest.mark.regression
    def test_search_cust_by_name(self, setup):
        self.logger.info('initiating Test005SearchCustName...')
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.login_pg = LoginPg(self.driver)
        self.login_pg.set_un(self.un)
        self.login_pg.set_pw(self.pw)
        self.login_pg.click_login()
        self.logger.info('login successful')
        time.sleep(2)

        self.logger.info('testing search_cust_by_name')
        self.add_cust = AddCust(self.driver)
        self.add_cust.click_cust_menu()
        self.add_cust.click_cust_cust_item()
        time.sleep(2)

        self.search = SearchCust(self.driver)
        self.test_data_name = 'brenda Lindgren'
        self.search.set_fname(self.test_data_name.split(' ')[0])
        self.search.set_lname(self.test_data_name.split(' ')[1])
        self.search.clk_search()
        time.sleep(5)
        status = self.search.search_cust_name(self.test_data_name)
        if status == True:
            self.logger.info('test_search_cust_by_name test passed')
            self.driver.quit()
            assert True
        else:
            self.logger.error('***test_search_cust_by_name test FAILED***')
            self.driver.save_screenshot(f'.//screengrabs//{self.today}test_search_cust_by_name.png')
            self.driver.quit()
            assert False


