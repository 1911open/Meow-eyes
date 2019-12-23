# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mine3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import pyecharts
import pandas as pd
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
import Mine
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
import os
from pyecharts_snapshot.main import make_a_snapshot
import threading
class Ui_Main3(object):
    def myshow(self):
        exec('self.widget.show()')
    def mytr(self):
        make_a_snapshot("2015_to_2018.html","2015_to_2018.png")

    def click2(self):
        conn = pymysql.connect(host='localhost', user='root', password='201314xIn', port=3306, db='maoyan',charset='utf8mb4')
        sql = "select * from films"
        db = pd.read_sql(sql, conn)
        y = [([0] * 13) for i in range(4)]
        t1 = threading.Thread(target=self.myshow)
        t2 = threading.Thread(target=self.mytr)
        for i in range(2015, 2019, 1):
            for j in range(1, 13, 1):
                y[i - 2015][j] = db[(db.year == i) & (db.month == j)].sum()["box_office"]
        x = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12]

        y1 = y[0]
        y2 = y[1]
        y3 = y[2]
        y4 = y[3]

        line = pyecharts.Line("2015 to 2018", width=1200, height=500)
        line.add("2015", x, y1)
        line.add("2016", x, y2)
        line.add("2017", x, y3)
        line.add("2018", x, y4)
        line.render("2015_to_2018.html")
        self.widget.load(QUrl('file:///2015_to_2018.html' ))
        t1.start()
        t2.start()
        #self.widget.show()
        #line.render("2015_to_2018.png")

    def click3(self):
        try:
            os.remove('2015_to_2018.html')
            os.remove('2015_to_2018.png')
        except:
            pass

    def click1(self):
        self.form.close()
        Form1 = QtWidgets.QMainWindow()
        self.ui = Mine.Ui_Mine()
        self.ui.setupUi(Form1)
        Form1.show()

    def setupUi(self, Main3):
        Main3.setObjectName("Main3")
        Main3.resize(1139, 829)
        Main3.setStyleSheet("border-image: url(:/M11.jpg);")
        Main3.setWindowFlags(Qt.FramelessWindowHint)
        self.form = Main3
        self.centralwidget = QtWidgets.QWidget(Main3)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 270, 1141, 531))
        self.widget.setObjectName("widget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, -10, 93, 241))
        self.pushButton_3.setStyleSheet("font: 40pt \"幼圆\";\n"
"color: rgb(255, 255, 0);\n"
"border-image: url(:/background2.png);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1010, 0, 93, 241))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("font: 40pt \"幼圆\";\n"
"color: rgb(255, 239, 2);\n"
"border-image: url(:/background2.png);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, -10, 93, 241))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("font: 40pt \"幼圆\";\n"
"color: rgb(255, 239, 2);\n"
"border-image: url(:/background2.png);")
        self.pushButton_2.setObjectName("pushButton_2")
        Main3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1139, 26))
        self.menubar.setObjectName("menubar")
        Main3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main3)
        self.statusbar.setObjectName("statusbar")
        Main3.setStatusBar(self.statusbar)

        self.retranslateUi(Main3)
        self.pushButton.clicked.connect(self.click1)
        self.pushButton_3.clicked.connect(self.click2)
        self.pushButton_2.clicked.connect(self.click3)
        QtCore.QMetaObject.connectSlotsByName(Main3)

    def retranslateUi(self, Main3):
        _translate = QtCore.QCoreApplication.translate
        Main3.setWindowTitle(_translate("Main3", "欢迎使用喵眼！"))
        self.pushButton_3.setText(_translate("Main3", "查\n"
"\n"
"看"))
        self.pushButton.setText(_translate("Main3", "返\n"
"\n"
"回"))
        self.pushButton_2.setText(_translate("Main3", "不\n"
"保\n"
"存"))

from PyQt5 import QtWebEngineWidgets
import myqrc_rc
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main3 = QtWidgets.QMainWindow()  # 注意，这里和我们一开始创建窗体时使用的界面类型相同
    ui = Ui_Main3()
    ui.setupUi(Main3)
    Main3.show()
    sys.exit(app.exec_())
