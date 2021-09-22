#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/9/20 13:10
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import sys
import os
p = u'/'.join(os.path.split(__file__)[:-1])
comm = u'maya "python \\"import sys;sys.path.append(\\\\"{}\\\\")\\""'.format(p)
os.system(comm)

