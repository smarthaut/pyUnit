#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/8 16:12
# @Author  : huanghe
# @Site    : 
# @File    : test_case_.py
# @Software: PyCharm

import os

#path = 'D:\python\test_cases\test_case'
#print(os.getcwd())
apath = r'D:\python\test_cases\test_case'
caselist = os.listdir(apath)
for a in  caselist:
    s = a.split('.')[1:][0]
    if s == 'py':
        comb = 'python ' + apath + '\\' + a
        os.system('%s 1>>log.txt 2>&1'%comb )
