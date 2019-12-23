# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import page1_1
import page1_2
import Dialog2
import Dialog1
import pygame
from PyQt5.QtCore import Qt
pygame.mixer.init()
class Ui_page1(object):


    def click4(self):
        pygame.mixer.music.load(r"page2_2.mp3")
        pygame.mixer.music.play()
        Form1 = QtWidgets.QDialog()
        self.ui = Dialog2.Ui_Dialog2()
        self.ui.setupUi(Form1)
        Form1.show()


    def click3(self):
        pygame.mixer.music.load(r"page2_1.mp3")
        pygame.mixer.music.play()
        Form1 = QtWidgets.QDialog()
        self.ui = Dialog1.Ui_Dialog1()
        self.ui.setupUi(Form1)
        Form1.show()
        information = "不再联系—冯提莫！"
        self.ui.label.setText(information)




    def click2(self):
        self.form.close()
        Form1 = QtWidgets.QMainWindow()
        self.ui = page1_2.Ui_page1_2()
        self.ui.setupUi(Form1)
        Form1.show()




    def click1(self):
        self.form.close()
        Form1 = QtWidgets.QMainWindow()
        self.ui = page1_1.Ui_page1_1()
        self.ui.setupUi(Form1)
        Form1.show()


    def setupUi(self, page1):
        page1.setObjectName("page1")
        page1.setWindowModality(QtCore.Qt.NonModal)
        page1.resize(789, 777)
        page1.setFocusPolicy(QtCore.Qt.NoFocus)
        page1.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        page1.setStyleSheet("border-image: url(:/button2.png);")
        self.form = page1
        self.centralwidget = QtWidgets.QWidget(page1)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(0, 0, 791, 131))
        self.logo.setStyleSheet("border-image: url(:/logo.png);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 280, 41, 41))
        self.label.setStyleSheet("border-image: url(:/load.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 280, 161, 41))
        self.pushButton.setStyleSheet("font: 20pt \"幼圆\";\n"
"color: rgb(255, 0, 0);\n"
"border-image: url(:/button3.png);")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 380, 41, 41))
        self.label_2.setStyleSheet("border-image: url(:/background3.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 380, 161, 41))
        self.pushButton_2.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 20pt \"幼圆\";\n"
"border-image: url(:/button3.png);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 480, 41, 41))
        self.label_3.setStyleSheet("border-image: url(:/contect.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 480, 161, 41))
        self.pushButton_3.setStyleSheet("border-image: url(:/button3.png);\n"
"color: rgb(255, 0, 0);\n"
"font: 20pt \"幼圆\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 580, 161, 41))
        self.pushButton_4.setStyleSheet("border-image: url(:/button3.png);\n"
"color: rgb(255, 0, 0);\n"
"font: 20pt \"幼圆\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 580, 41, 41))
        self.label_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.339795 rgba(255, 0, 0, 255), stop:0.339799 rgba(255, 255, 255, 255), stop:0.662444 rgba(255, 255, 255, 255), stop:0.662469 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 255));\n"
"border-image: url(:/button4.png);")
        self.label_4.setMidLineWidth(0)
        self.label_4.setText("")
        self.label_4.setIndent(0)
        self.label_4.setObjectName("label_4")
        page1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(page1)
        self.statusbar.setObjectName("statusbar")
        page1.setStatusBar(self.statusbar)

        self.retranslateUi(page1)
        self.pushButton.clicked.connect(self.click1)
        self.pushButton_2.clicked.connect(self.click2)
        self.pushButton_3.clicked.connect(self.click3)
        self.pushButton_4.clicked.connect(self.click4)
        QtCore.QMetaObject.connectSlotsByName(page1)

    def retranslateUi(self, page1):
        _translate = QtCore.QCoreApplication.translate
        page1.setWindowTitle(_translate("page1", "欢迎来到喵眼2.0！"))
        self.pushButton.setText(_translate("page1", "注册"))
        self.pushButton_2.setText(_translate("page1", "登陆"))
        self.pushButton_3.setText(_translate("page1", "联系作者"))
        self.pushButton_4.setText(_translate("page1", "反馈bug"))

import myqrc_rc
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    page1 = QtWidgets.QMainWindow()  # 注意，这里和我们一开始创建窗体时使用的界面类型相同
    ui = Ui_page1()
    ui.setupUi(page1)
    page1.show()
    sys.exit(app.exec_())