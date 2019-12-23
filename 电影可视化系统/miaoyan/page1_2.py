# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page1_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import page1
import Dialog1
import pymysql
import Mine
from hashlib import sha1

def load(name,pwd):
    db = pymysql.connect(host='localhost',port=3306,user='root',passwd='201314xIn',db='maoyan',charset='utf8')
# 接收用户输入
    res = name
    # 对密码加密
    # m = sha1()
    # s = m.update(pwd.encode("utf-8"))
    # print(s)
    pwd2=sha1(pwd.encode('utf-8')).hexdigest()
    # 根据用户名查询密码

    sql = 'select password from userinfo where name=%s'
    cursor = db.cursor()
    cursor.execute(sql,res)
    psw = cursor.fetchall()
    db.commit()
    cursor.close()
    db.close()
    if psw == ():
        return 0
    elif psw[0][0] == pwd2:
        return 1
    elif psw[0][0] != pwd2:
        return 3
    else:
        return 2

class Ui_page1_2(object):

    def click2(self):
        name = self.input_zh.toPlainText()
        pwd = self.input_zh_4.toPlainText()
        Form2 = QtWidgets.QDialog()
        self.ui1 = Dialog1.Ui_Dialog1()
        self.ui1.setupUi(Form2)
        flag = load(name,pwd)
        if flag == 0:
            information = "账号不存在"
            Form2.show()
            self.ui1.label.setText(information)
        elif flag == 3:
            information = "密码错误"
            Form2.show()
            self.ui1.label.setText(information)

        elif flag == 2:
            information = "输入不能为空"
            Form2.show()
            self.ui1.label.setText(information)
        else:
            Form2.close()
            self.form.close()
            Form1 = QtWidgets.QMainWindow()
            self.ui = Mine.Ui_Mine()
            self.ui.setupUi(Form1)
            Form1.show()

    def click1(self):
        self.form.close()
        Form1 = QtWidgets.QMainWindow()
        self.ui = page1.Ui_page1()
        self.ui.setupUi(Form1)
        Form1.show()

    def setupUi(self, page1_2):
        page1_2.setObjectName("page1_2")
        page1_2.resize(549, 535)
        page1_2.setStyleSheet("border-image: url(:/M8.png);")
        self.form = page1_2
        self.centralwidget = QtWidgets.QWidget(page1_2)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 541, 101))
        self.label.setStyleSheet("border-image: url(:/logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.input_zh = QtWidgets.QTextEdit(self.centralwidget)
        self.input_zh.setGeometry(QtCore.QRect(230, 180, 171, 31))
        self.input_zh.setStyleSheet("border-image: url(:/M9.png);")
        self.input_zh.setObjectName("input_zh")
        self.input_zh_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.input_zh_4.setGeometry(QtCore.QRect(230, 230, 171, 31))
        self.input_zh_4.setStyleSheet("border-image: url(:/M9.png);")
        self.input_zh_4.setObjectName("input_zh_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 180, 131, 31))
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 20pt \"幼圆\";\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.495 rgba(255, 255, 255, 255), stop:0.505 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 230, 131, 31))
        self.label_3.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 20pt \"幼圆\";\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.495 rgba(255, 255, 255, 255), stop:0.505 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 320, 221, 51))
        self.pushButton.setStyleSheet("font: 20pt \"华文琥珀\";\n"
"color: rgb(0, 255, 255);\n"
"border-image: url(:/M7.png);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 410, 221, 51))
        self.pushButton_2.setStyleSheet("font: 20pt \"华文琥珀\";\n"
"color: rgb(0, 255, 255);\n"
"border-image: url(:/M7.png);")
        self.pushButton_2.setObjectName("pushButton_2")
        page1_2.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(page1_2)
        self.statusbar.setObjectName("statusbar")
        page1_2.setStatusBar(self.statusbar)

        self.retranslateUi(page1_2)
        self.pushButton.clicked.connect(self.click2)
        self.pushButton_2.clicked.connect(self.click1)
        QtCore.QMetaObject.connectSlotsByName(page1_2)

    def retranslateUi(self, page1_2):
        _translate = QtCore.QCoreApplication.translate
        page1_2.setWindowTitle(_translate("page1_2", "MainWindow"))
        self.label_2.setText(_translate("page1_2", "  账号"))
        self.label_3.setText(_translate("page1_2", "  密码"))
        self.pushButton.setText(_translate("page1_2", "    登陆"))
        self.pushButton_2.setText(_translate("page1_2", "    返回"))

import myqrc_rc
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    page1_2 = QtWidgets.QMainWindow()  # 注意，这里和我们一开始创建窗体时使用的界面类型相同
    ui = Ui_page1_2()
    ui.setupUi(page1_2)
    page1_2.show()
    sys.exit(app.exec_())
