#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Sizepeng Zhao

from PyQt5 import QtCore, QtGui, QtWidgets
from translate import trans

#创建一个翻译类的对象
tran = trans()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(726, 569)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(542, 260, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 300, 621, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 60, 621, 191))
        self.textEdit.setObjectName("textEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 30, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(50, 260, 141, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 726, 26))
        self.menubar.setObjectName("menubar")
        self.menuZszp = QtWidgets.QMenu(self.menubar)
        self.menuZszp.setObjectName("menuZszp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuZszp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.comboBox.currentIndexChanged.connect(self.selectionchange_f)
        self.comboBox_2.currentIndexChanged.connect(self.selectionchange_t)
        self.pushButton.clicked.connect(self.transbutton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "翻译"))
        self.comboBox.setItemText(0, _translate("MainWindow", "自动检测"))
        self.comboBox.setItemText(1, _translate("MainWindow", "中文"))
        self.comboBox.setItemText(2, _translate("MainWindow", "英语"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "中文"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "英语"))
        self.menuZszp.setTitle(_translate("MainWindow", "zszp翻译"))

    #选择待翻译文本的语言
    def selectionchange_f(self):
        if self.comboBox.currentText() == "自动检测":
            trans.change_fl(tran, 'auto')
        elif self.comboBox.currentText() == "中文":
            trans.change_fl(tran, 'zh')
        elif self.comboBox.currentText() == "英语":
            trans.change_fl(tran, 'en')

    #选择翻译出来的语言
    def selectionchange_t(self):
        if self.comboBox_2.currentText() == "中文":
            trans.change_tl(tran, 'zh')
        elif self.comboBox_2.currentText() == "英语":
            trans.change_tl(tran, 'en')

    #当翻译按钮按下，开始翻译
    def transbutton(self):
        #得到待翻译的文本 q
        q=self.textEdit.toPlainText()
        #通过翻译类的函数翻译q
        self.textBrowser.setText(tran.translate(q))