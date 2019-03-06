# -*- coding:utf-8 -*-
import unittest
import time
from selenium import webdriver


class PythonOrgSearch1(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_search_in_python_org1(self):
        browser = self.browser
        file_path = 'https://pan.baidu.com/'
        browser.get(file_path)
        browser.minimize_window()
        print("login "+browser.title+"url "+browser.current_url)
        browser.find_element_by_id("txtUserName").send_keys("admin")
        browser.find_element_by_id("txtPassword").send_keys("cngrain_wwww2016")
        browser.find_element_by_id("imgBtnLogin").click()
        #browser.find_element_by_id("lnkClose").click()
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()