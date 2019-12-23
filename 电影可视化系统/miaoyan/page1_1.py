# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page1_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import page1
import pymysql
import hashlib
import Dialog1


def regisster_(name,pwd1,pwd2):

    if pwd1 != pwd2:
        return 0
    elif pwd1 == "":
        return 10
    try:
        db = pymysql.connect(host='localhost', port=3306, user='root', passwd='201314xIn', db='maoyan', charset='utf8')
        cursor = db.cursor()
        sql = "insert into userinfo(name,password) values(%s,%s)"
        pwd = hashlib.sha1(pwd2.encode("utf-8")).hexdigest()
        print(pwd)
        res = [name,pwd]
        print(res)
        cursor.execute(sql,res)
        db.commit()
        cursor.close()
        db.close()
        return 1
    except:
        pass

class Ui_page1_1(object):
    def click2(self):
        Form1 = QtWidgets.QDialog()
        self.ui = Dialog1.Ui_Dialog1()
        self.ui.setupUi(Form1)
        Form1.show()
        name = self.input_zh.toPlainText()
        pwd1 =  self.Input_mm.toPlainText()
        pwd2 = self.input_qrmm.toPlainText()
        if regisster_(name,pwd1,pwd2) == 0:
            information = "两次密码不一致"
        elif regisster_(name,pwd1,pwd2) == 10:
            information = "输入不能为空"
        else:
            information = "注册成功"
        self.ui.label.setText(information)

    def click1(self):
        self.form.close()
        Form1 = QtWidgets.QMainWindow()
        self.ui = page1.Ui_page1()
        self.ui.setupUi(Form1)
        Form1.show()


    def setupUi(self, page1_1):
        page1_1.setObjectName("page1_1")
        page1_1.resize(873, 420)
        page1_1.setStyleSheet("border-image: url(:/button3.png);")
        self.form = page1_1
        self.centralwidget = QtWidgets.QWidget(page1_1)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 461, 420))
        self.label.setStyleSheet("border-image: url(:/logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.Input_mm = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Input_mm.setGeometry(QtCore.QRect(640, 130, 171, 31))
        self.Input_mm.setStyleSheet("border-image: url(:/background3.png);")
        self.Input_mm.setObjectName("Input_mm")
        self.input_qrmm = QtWidgets.QTextEdit(self.centralwidget)
        self.input_qrmm.setGeometry(QtCore.QRect(640, 200, 171, 31))
        self.input_qrmm.setStyleSheet("border-image: url(:/background3.png);")
        self.input_qrmm.setObjectName("input_qrmm")
        self.input_zh = QtWidgets.QTextEdit(self.centralwidget)
        self.input_zh.setGeometry(QtCore.QRect(640, 60, 171, 31))
        self.input_zh.setStyleSheet("border-image: url(:/background3.png);")
        self.input_zh.setObjectName("input_zh")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 60, 131, 31))
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 20pt \"幼圆\";\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.495 rgba(255, 255, 255, 255), stop:0.505 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")
        self.label_2.setObjectName("label_2")
        self.B2_zc = QtWidgets.QPushButton(self.centralwidget)
        self.B2_zc.setGeometry(QtCore.QRect(550, 327, 71, 41))
        self.B2_zc.setStyleSheet("font: 20pt \"方正姚体\";\n"
"color: rgb(255, 85, 0);")
        self.B2_zc.setObjectName("B2_zc")
        self.B1_zc = QtWidgets.QPushButton(self.centralwidget)
        self.B1_zc.setGeometry(QtCore.QRect(700, 327, 71, 41))
        self.B1_zc.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 20pt \"方正姚体\";")
        self.B1_zc.setObjectName("B1_zc")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, 130, 131, 31))
        self.label_3.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 20pt \"幼圆\";\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.495 rgba(255, 255, 255, 255), stop:0.505 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 200, 131, 31))
        self.label_4.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 20pt \"幼圆\";\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.495 rgba(255, 255, 255, 255), stop:0.505 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));")
        self.label_4.setObjectName("label_4")
        page1_1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(page1_1)
        self.statusbar.setObjectName("statusbar")
        page1_1.setStatusBar(self.statusbar)

        self.retranslateUi(page1_1)
        self.B1_zc.clicked.connect(self.click1)
        self.B2_zc.clicked.connect(self.click2)
        QtCore.QMetaObject.connectSlotsByName(page1_1)

    def retranslateUi(self, page1_1):
        _translate = QtCore.QCoreApplication.translate
        page1_1.setWindowTitle(_translate("page1_1", "MainWindow"))
        self.label_2.setText(_translate("page1_1", "  账号"))
        self.B2_zc.setText(_translate("page1_1", "注册"))
        self.B1_zc.setText(_translate("page1_1", "返回"))
        self.label_3.setText(_translate("page1_1", "  密码"))
        self.label_4.setText(_translate("page1_1", "确认密码"))

import myqrc_rc
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    page1_1 = QtWidgets.QMainWindow()  # 注意，这里和我们一开始创建窗体时使用的界面类型相同
    ui = Ui_page1_1()
    ui.setupUi(page1_1)
    page1_1.show()
    sys.exit(app.exec_())