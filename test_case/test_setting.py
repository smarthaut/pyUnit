#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/8 16:03
# @Author  : huanghe
# @Site    : 
# @File    : test_setting.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest,time
import HTMLTestRunner

class BaiduSetting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_baidu_setting(self):
        u"""百度设置用例"""
        driver = self.driver
        driver.get(self.base_url+'/gaoji/preferences.html')
        m = driver.find_element_by_name("NR")
        m.find_element_by_xpath("//option[@value='10']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@value='保存设置']").click()
        time.sleep(5)
        ActionChains(driver).move_by_offset(710, 350).click()
        #driver.switch_to.alert.accept()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__=="__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(BaiduSetting("test_baidu_setting"))
    filename = r'D:\python\test_cases\demo02.html'
    f = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=f,
        title='Repot_title',
        description='Repot_description'
    )
    runner.run(testunit)