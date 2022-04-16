#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/9/20 16:22
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
try:
    import maya.standalone

    maya.standalone.initialize(name='python')
except:
    pass

import cpgui.pop_ups as pop_ups
pop_ups.input_text()
pop_ups.input_int()
pop_ups.input_float()
pop_ups.input_double()
pop_ups.input_multiLine_text()
pop_ups.confirm()
