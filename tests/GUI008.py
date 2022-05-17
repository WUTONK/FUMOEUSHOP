# file: custom_signal.py
#!/usr/bin/python

"""
ZetCode PyQt6 tutorial

In this example, we show how to
emit a custom signal.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
from PyQt6.QtCore import pyqtSignal, QObject
from PyQt6.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):

    closeApp = pyqtSignal() #把closeApp自定义为pyqt信号


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.c = Communicate() #把外部类绑定
        self.c.closeApp.connect(self.close) #将外部类的自定义信号锚定到QMainWindow.close()关闭插槽上

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Emit signal')
        self.show()

    #使用pyqt内置的点击鼠标监听函数
    def mousePressEvent(self, e):

        self.c.closeApp.emit()#发送信号


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()