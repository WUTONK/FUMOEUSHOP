"""
关于作者页面
"""
import webbrowser
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLCDNumber, QSlider,QVBoxLayout, QApplication)


class GUI():

    def initUI():
        pass

class web_link():

    def Check_link_open_web(linkType):
        
        name_url = 'https://github.com/WUTONK'
        git_url = 'https://github.com/WUTONK/FUMOEUSHOP'
        contact_url =  'https://WUTONK.xyz' 

        if linkType == 'name':
            #调用默认浏览器在新标签页打开git主页链接
            webbrowser.open(name_url, new=2, autoraise=True)
        if linkType == "git":
            webbrowser.open(git_url, new=2, autoraise=True)
        if linkType == "contact": 
            webbrowser.open(contact_url, new=2, autoraise=True)
