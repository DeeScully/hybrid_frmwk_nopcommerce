import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SearchCust:
    #locators
    txt_fld_email_id = r'SearchEmail'
    txt_fld_fname_id = r'SearchFirstName'
    txt_fld_lname_id = r'SearchLastName'
    btn_search_id = r'search-customers'

    tbl_search_results_xpath = r'.//table[@role="grid"]'
    tbl_custs_xpath = r'.//table[@id="customers-grid"]'
    tbl_custs_rows_xpath = r'.//table[@id="customers-grid"]/tbody/tr'
    tbl_custs_cols_xpath = r'.//table[@id="customers-grid"]/tbody/tr/td'

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        email_fld = self.driver.find_element(By.ID, self.txt_fld_email_id)
        email_fld.clear()
        email_fld.send_keys(email)

    def set_fname(self, fname):
        fname_fld = self.driver.find_element(By.ID, self.txt_fld_fname_id)
        fname_fld.clear()
        fname_fld.send_keys(fname)

    def set_lname(self, lname):
        lname_fld = self.driver.find_element(By.ID, self.txt_fld_lname_id)
        lname_fld.clear()
        lname_fld.send_keys(lname)

    def clk_search(self):
        self.driver.find_element(By.ID, self.btn_search_id).click()

    def get_num_rows(self):
        return len(self.driver.find_elements(By.XPATH, self.tbl_custs_rows_xpath))

    def get_num_cols(self):
        return len(self.driver.find_elements(By.XPATH, self.tbl_custs_cols_xpath))

    def search_cust_email(self, email):
        email_stdzd = email.lower()
        flag = False
        for i in range(1, self.get_num_rows()+1):
            table = self.driver.find_element_by_xpath(self.tbl_search_results_xpath)
            email_result_in_table = table.find_element(By.XPATH,f'//table[@id="customers-grid"]/tbody/tr[{i}]/td[2]').text
            email_result_in_table_stdzd = email_result_in_table.lower()
            print('email is', email)
            print('found in field is', email_result_in_table)
            if email_stdzd == email_result_in_table_stdzd:
                flag = True
                break
        return flag

    def search_cust_name(self, name):
        name_stdzd = name.lower()
        flag = False
        for i in range(1, self.get_num_rows()+1):
            table = self.driver.find_element(By.XPATH, self.tbl_custs_xpath)
            name_result_in_table = table.find_element(By.XPATH,f'//table[@id="customers-grid"]/tbody/tr[{i}]/td[3]').text
            name_result_in_table_stdzd = name_result_in_table.lower()
            print('name is', name)
            print('found in field is', name_result_in_table)
            if name_stdzd == name_result_in_table_stdzd:
                flag = True
                break
        return flag