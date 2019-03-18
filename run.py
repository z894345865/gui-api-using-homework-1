#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Sizepeng Zhao

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from gui import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())