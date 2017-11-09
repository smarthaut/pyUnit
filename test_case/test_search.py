#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/8 15:48
# @Author  : huanghe
# @Site    : 
# @File    : test_search.py
# @Software: PyCharm
#如果使用Pycharm不要run unittest
from selenium import webdriver
import unittest,time
import HTMLTestRunner


class BaiduSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_baidu_search(self):
        u"""百度搜索用例"""
        driver = self.driver
        driver.get(self.base_url+'/')
        filename = r'D:\python\test_cases\test_case\kw.png'
        try:
            driver.find_element_by_id('kw').send_keys('aaa')
        except:
            png = driver.get_screenshot_as_png()
            with open(filename, 'wb') as f:
                f.write(png)
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()
        #self.assertEqual([],self.verificationErrors)

if __name__=="__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(BaiduSearch("test_baidu_search"))
    filename = r'D:\python\test_cases\demo01.html'
    f = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=f,
        title='Repot_title',
        description='Repot_description'
    )
    runner.run(testunit)