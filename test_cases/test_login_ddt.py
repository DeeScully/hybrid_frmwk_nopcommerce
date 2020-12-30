import pytest
from selenium import webdriver
from page_objects.login_pg import LoginPg
from selenium.webdriver.common.keys import Keys
from datetime import date
from utils.read_properties import ReadConfig
from utils.custom_logger import LogGen
from utils import XLUtils
import time

#run tests by using command pytest -v --html=reports\report.html test_cases/test_login_ddt.py --browser firefox
class Test002DDTLogin:
    base_url = ReadConfig.get_app_url()
    path = '.\\test_data\\loginData.xlsx'

    today = date.today().strftime("%Y%m%d")
    logger = LogGen.log_gen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info('***Test002DDTLogin***')
        self.logger.info('test_login_ddt...')
        self.driver = setup
        self.driver.get(self.base_url)
        self.login_pg = LoginPg(self.driver)

        #this is where you grab the data from the xls file to drive the testing
        self.rows = XLUtils.get_row_count(self.path, 'Sheet1')
        results_lst = list()
        for row in range(2, self.rows + 1):
            self.un = XLUtils.read_data(self.path, 'Sheet1', row, 1)
            self.pw = XLUtils.read_data(self.path, 'Sheet1', row, 2)
            self.expected_result = XLUtils.read_data(self.path, 'Sheet1', row, 3)
            self.login_pg.set_un(self.un)
            self.login_pg.set_pw(self.pw)
            self.login_pg.click_login()
            time.sleep(5)

            actual_dashboardpg_title = self.driver.title
            expected_dashboardpg_title = 'Dashboard / nopCommerce administration'
            if actual_dashboardpg_title != expected_dashboardpg_title:
                if self.expected_result == 'Pass':
                    self.logger.error(f'test_login_ddt row:{row} test FAILED')
                    results_lst.append('Fail')
                elif self.expected_result == 'Fail':
                    self.logger.info(f'test_login_ddt row:{row} test passed')
                    results_lst.append('Pass')
            else:
                if self.expected_result == 'Pass':
                    self.logger.info(f'test_login_ddt row:{row} test passed')
                    self.login_pg.click_logout()
                    results_lst.append('Pass')
                elif self.expected_result == 'Fail':
                    self.logger.error(f'test_login_ddt row:{row} test FAILED')
                    self.login_pg.click_logout()
                    results_lst.append('Fail')

        if 'Fail' in results_lst:
            self.logger.error('test_login_ddt test FAILED')
            self.driver.quit()
            assert False
        else:
            self.logger.info('test_login_ddt test passed')
            self.driver.quit()
            assert True

        self.logger.info('Test002DDTLogin tests completed')