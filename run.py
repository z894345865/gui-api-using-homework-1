#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Sizepeng Zhao

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from gui import *

if __name__ == "__main__":
    #建立应用对象
    app = QApplication(sys.argv)
    #建立顶层窗口
    mainwindow = QMainWindow()
    #建立子窗口（由自己设计）
    ui = Ui_MainWindow()
    #将子窗口放入顶层窗口
    ui.setupUi(mainwindow)
    #显示窗口
    mainwindow.show()
    #程序一直循环直到窗口被关闭
    sys.exit(app.exec_())