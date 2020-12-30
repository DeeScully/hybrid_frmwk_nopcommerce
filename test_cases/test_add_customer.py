import pytest
from page_objects.login_pg import LoginPg
from page_objects.add_cust_pg import AddCust
from datetime import date
from utils.read_properties import ReadConfig
from utils.custom_logger import LogGen
import string
import random
import time
'''run test pytest -v --html=reports\insert_date\report.html test_cases\test_add_customer.py'''

class Test003AddCust:
    base_url = ReadConfig.get_app_url()
    un = ReadConfig.get_username()
    pw = ReadConfig.get_password()
    today = date.today().strftime("%Y%m%d")
    logger = LogGen.log_gen()

    @pytest.mark.sanity
    def test_add_cust(self, setup):
        self.logger.info('initiating Test003AddCust...')
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.login_pg = LoginPg(self.driver)
        self.login_pg.set_un(self.un)
        self.login_pg.set_pw(self.pw)
        self.login_pg.click_login()
        self.logger.info('login successful')
        time.sleep(2)

        self.logger.info('testing add_cust')
        self.add_cust = AddCust(self.driver)
        self.add_cust.click_cust_menu()
        self.add_cust.click_cust_cust_item()
        time.sleep(2)
        self.add_cust.click_add_new()

        self.logger.info('providing cust info')
        self.email = rand_gen() + '@test.test'
        self.add_cust.set_email(self.email)
        self.add_cust.set_pw('password1')
        self.add_cust.set_fname('first')
        self.add_cust.set_lname('last')
        self.add_cust.set_gender('Male')
        self.add_cust.set_dob('01/02/1970')
        self.add_cust.set_company_name('Test Co')
        self.add_cust.set_cust_roles('Guests')
        self.add_cust.set_mgr_of_vend('Vendor 2')
        self.add_cust.set_admin_content('Test content...')
        self.add_cust.clk_save()
        self.logger.info('saving cust info')

        self.logger.info('validating test')
        #save body of page into a var
        self.msg = self.driver.find_element_by_tag_name('body').text
        if 'customer has been added successfully' in self.msg:
            self.logger.info('add_cust test passed')
            assert True
        else:
            self.logger.error('***add_cust test FAILED***')
            self.driver.save_screenshot(f'.//screengrabs//{self.today}test_add_cust.png')
            assert False

        self.driver.quit()




def rand_gen(max_size = 12, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choices(chars, k = random.randint(8, max_size)))



