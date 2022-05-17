# file: signals_slots.py
#!/usr/bin/python

"""
ZetCode PyQt6 tutorial

本例中，把 QSlider 触发的事件和 QLCDNumber 插槽绑定起来

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLCDNumber, QSlider,
        QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
       

    def initUI(self):

        self.lcd = QLCDNumber(self)
        self.sld = QSlider(Qt.Orientation.Horizontal, self) #这里定义了一个滑块

        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addWidget(self.sld)

        self.setLayout(vbox)
        self.sld.valueChanged.connect(self.lcd.display) #把滑块的值改变链接到lcd

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Signal and slot')
        self.show()


    def keyPressEvent(self, key): #这里key是接受按键的变量(事件对象)
        
        if key.key() == Qt.Key.Key_Escape.value: #以监听判断实现槽（调用关闭）
            self.sld.valueChanged(10)

def main():
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()