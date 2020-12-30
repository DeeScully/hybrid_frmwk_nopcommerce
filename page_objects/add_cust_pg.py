import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class AddCust:
    #locators
    menu_cust_xpath = './/a[@href="#"]/span[contains(text(), "Customers")]'
    menu_cust_cust_xpath = './/span[@class="menu-item-title"][contains(text(), "Customers")]'
    btn_add_new_xpath = './/a[@class="btn bg-blue"]'
    txt_fld_email_id = 'Email'
    txt_fld_pw_name = 'Password'
    txt_fld_first_name_id = 'FirstName'
    txt_fld_last_name_name = 'LastName'
    radio_male_id = 'Gender_Male'
    radio_female_id = 'Gender_Female'
    txt_fld_dob_name = 'DateOfBirth'
    txt_fld_company_name = 'Company'
    chk_bx_tax_exempt_id = 'IsTaxExempt'
    drp_nwsltr_id = 'SelectedNewsletterSubscriptionStoreIds_taglist'
    drp_item_store_name_xpath = './/li[contains(text(), "Your store name")]'
    drp_item_test_store_2_xpath = './/li[contains(text(), "Test store 2")]'
    txt_fld_cust_roles_xpath = './/div[@class="k-multiselect-wrap k-floatwrap"]'
    lst_item_admin_xpath = './/li[contains(text(), "Administrators")]'
    lst_item_forum_mods_xpath = './/li[contains(text(), "Forum Moderators")]'
    lst_item_guests_xpath = './/li[contains(text(), "Guests")]'
    lst_item_registered_xpath = './/li[contains(text(), "Registered")]'
    lst_item_vendors_xpath = './/li[contains(text(), "Vendors")]'
    drp_mgr_of_vend_id = 'VendorId'
    chk_bx_active_id = 'Active'
    txt_fld_admin_comment_id = 'AdminComment'
    btn_save_name = 'save'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_cust_menu(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.menu_cust_xpath))).click()

    def click_cust_cust_item(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.menu_cust_cust_xpath))).click()

    def click_add_new(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_add_new_xpath))).click()

    def set_email(self, email):
        email_fld = self.wait.until(EC.visibility_of_element_located((By.ID, self.txt_fld_email_id)))
        email_fld.clear()
        email_fld.send_keys(email)

    def set_pw(self, pw):
        pw_fld = self.wait.until(EC.visibility_of_element_located((By.NAME, self.txt_fld_pw_name)))
        pw_fld.clear()
        pw_fld.send_keys(pw)

    def set_fname(self, fname):
        fname_fld = self.wait.until(EC.visibility_of_element_located((By.ID, self.txt_fld_first_name_id)))
        fname_fld.clear()
        fname_fld.send_keys(fname)

    def set_lname(self, lname):
        lname_fld = self.wait.until(EC.visibility_of_element_located((By.NAME, self.txt_fld_last_name_name)))
        lname_fld.clear()
        lname_fld.send_keys(lname)

    def set_gender(self, gender):
        if gender == 'Male':
            self.wait.until(EC.element_to_be_clickable((By.ID, self.radio_male_id))).click()
        elif gender == 'Female':
            self.wait.until(EC.element_to_be_clickable((By.ID, self.radio_female_id))).click()
        else: self.wait.until(EC.element_to_be_clickable((By.ID, self.radio_male_id))).click()

    def set_dob(self, dob):
        dob_fld = self.wait.until(EC.visibility_of_element_located((By.NAME, self.txt_fld_dob_name)))
        dob_fld.clear()
        dob_fld.send_keys(dob)

    def set_company_name(self, compname):
        compname_fld = self.wait.until(EC.visibility_of_element_located((By.NAME, self.txt_fld_company_name)))
        compname_fld.clear()
        compname_fld.send_keys(compname)

    def set_cust_roles(self, role):
        #click into fld to view selections
        self.driver.find_elements_by_xpath(self.txt_fld_cust_roles_xpath)[1].click()
        # self.wait.until(EC.elements_to_be_clickable((By.XPATH, self.txt_fld_cust_roles_xpath))).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lst_item_registered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lst_item_admin_xpath)
        elif role == 'Forum Moderators':
            self.listitem = self.driver.find_element(By.XPATH, self.lst_item_forum_mods_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lst_item_vendors_xpath)
        else:
            # rem the default registered selection
            self.driver.find_element(By.XPATH, './/*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]').click()
            self.listitem = self.driver.find_element(By.XPATH,self.lst_item_guests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def set_mgr_of_vend(self, val):
        drp = Select(self.wait.until(EC.element_to_be_clickable((By.ID, self.drp_mgr_of_vend_id))))
        drp.select_by_visible_text(val)

    def set_admin_content(self, content):
        admin_content_fld = self.driver.find_element(By.ID, self.txt_fld_admin_comment_id)
        admin_content_fld.clear()
        admin_content_fld.send_keys(content)

    def clk_save(self):
        self.wait.until(EC.element_to_be_clickable((By.NAME, self.btn_save_name))).click()








