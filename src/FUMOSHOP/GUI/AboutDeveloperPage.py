"""
关于作者页面
"""
from os import link
import webbrowser

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLCDNumber, QSlider,QVBoxLayout, QApplication)

linkType = 'name'


def Check_link_open_web(linkType):
    
    name_url = 'https://github.com/WUTONK'
    git_url = 'https://github.com/WUTONK/FUMOEUSHOP'

    if linkType == 'name':
        webbrowser.open(name_url, new=2, autoraise=True)#在新标签页打开git主页链接 
    if linkType == "git":
        webbrowser.open(git_url, new=2, autoraise=True)

Check_link_open_web(linkType)