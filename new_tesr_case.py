#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/9 13:11
# @Author  : huanghe
# @Site    : 
# @File    : new_tesr_case.py
# @Software: PyCharm
import HTMLTestRunner
import unittest,doctest
from test_case.test_setting import BaiduSetting
from test_case.test_search import BaiduSearch

suit = doctest.DocTestSuite()
suit.addTest(unittest.makeSuite(BaiduSearch))
suit.addTest(unittest.makeSuite(BaiduSetting))
filename = r'D:\python\test_cases\results.html'
f = open(filename,'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=f,
    title = 'Report_title',
    description='Descryption'
)
runner.run(suit)