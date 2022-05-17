# file: reimplement_handler.py
#!/usr/bin/python

"""
ZetCode PyQt6 tutorial

本例中，我们重新实现了一个事件处理器。

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Event handler')
        self.show()


    def keyPressEvent(self, key): #这里key是接受按键的变量(事件对象)
        
        if key.key() == Qt.Key.Key_Escape.value: #以监听判断实现槽（调用关闭）
            self.close()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()