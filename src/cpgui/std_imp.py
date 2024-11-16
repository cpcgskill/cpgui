#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/9/20 12:54
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
try:
    from PyQt6.QtWidgets import *
    from PyQt6.QtCore import *
    from PyQt6.QtGui import *
    gui_runtime = 'PyQt6'
except ImportError:
    try:
        from PySide6.QtGui import *
        from PySide6.QtCore import *
        from PySide6.QtWidgets import *
        gui_runtime = 'PySide6'
    except ImportError:
        try:
            from PyQt5.QtWidgets import *
            from PyQt5.QtCore import *
            from PyQt5.QtGui import *
            gui_runtime = 'PyQt5'
        except ImportError:
            try:
                from PySide2.QtGui import *
                from PySide2.QtCore import *
                from PySide2.QtWidgets import *
                gui_runtime = 'PySide2'
            except ImportError:
                from PySide.QtGui import *
                from PySide.QtCore import *
                gui_runtime = 'PySide'

if gui_runtime == 'PyQt6':
    from PyQt6.QtSvgWidgets import QSvgWidget
    from PyQt6.QtSvg import QSvgRenderer
elif gui_runtime == 'PySide6':
    from PySide6.QtSvgWidgets import QSvgWidget
    from PySide6.QtSvg import QSvgRenderer
elif gui_runtime == 'PyQt5':
    from PyQt5.QtSvg import QSvgWidget, QSvgRenderer
elif gui_runtime == 'PySide2':
    from PySide2.QtSvg import QSvgWidget, QSvgRenderer
else:
    from PySide.QtSvg import QSvgWidget, QSvgRenderer

try:
    from shiboken6 import *
except ImportError:
    try:
        from shiboken2 import *
    except ImportError:
        from shiboken import *

import sys
import maya.OpenMayaUI as OpenMayaUI

deleteWidget = delete
try:
    if sys.version_info.major >= 3:
        mui = wrapInstance(int(OpenMayaUI.MQtUtil.mainWindow()), QWidget)
    else:
        mui = wrapInstance(long(OpenMayaUI.MQtUtil.mainWindow()), QWidget)
except:
    mui = None