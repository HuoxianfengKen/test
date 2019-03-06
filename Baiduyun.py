#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#加载unittest模块
import unittest
import time

#加载HTMLTestRunner,用于生成HTNLreuslt
import HTMLTestRunner

#百度云测试类
class BaiduYun(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(30)
        self.base_url = "https://yun.baidu.com/"
        self.verficationErrors=[]
        self.accept_next_elert = True

    def tearDown(self):
        self.browser.quit()
        self.assertEqual([],self.verficationErrors)

    def test_Login(self):
        browser = self.browser
        browser.get(self.base_url)
        #百度云登录
        browser.find_element_by_id("TANGRAM__PSP_4__footerULoginBtn").click()
        username = browser.find_element_by_name("userName")
        username.clear()
        username.send_keys("1084035413")
        username.send_keys(Keys.TAB)
        time.sleep(5)
        password = browser.find_element_by_name("password")
        password.send_keys("qq13820659551")
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        browser.close()

    def test_Register(self):
        browser = self.browser
        browser.get(self.base_url)
        #立刻注册百度云账号
        browser.find_element_by_link_text("立即注册").click()
        time.sleep(5)
        browser.close()

    def test_Link(self):
        browser = self.browser
        browser.get(self.base_url)
        #会员中心
        browser.find_element_by_link_text("会员中心").click()
        time.sleep(5)
        browser.close()

if __name__ == '__main__':
    # unittest.main()
    testunit = unittest.TestSuite()
    # 将测试用例加入到测试容器中
    testunit.addTest(BaiduYun("test_Login"))
    testunit.addTest(BaiduYun("test_Register"))
    testunit.addTest(BaiduYun("test_Link"))
    # 获取当前时间以保存测试用例
    now = time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))
    # 打开一个文件保存测试结果
    fp = open("result"+now+".html",'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='test result',description=u'result:')
    runner.run(testunit)
    fp.close()
