# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mine2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Mine
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
import pandas as pd
import pymysql
import os
from pyecharts import WordCloud
from PyQt5.QtCore import Qt
from pyecharts_snapshot.main import make_a_snapshot
import threading
class Ui_Mine2(object):
    def myshow(self):
        exec('self.widget.show()')

    def mytr(self,year,top):
        make_a_snapshot("wc%d.html" % (year * 100 + top),("wc%d.png" % (year * 100 + top)))



    def click3(self):
        year = int(self.comboBox.currentText())
        top = int(self.comboBox_2.currentText())
        try:
            os.remove('wc%d.html'%(year*100+top))
            os.remove('wc%d.png' % (year * 100 + top))
        except:
            pass

    def click2(self):
        year = int(self.comboBox.currentText())
        top = int(self.comboBox_2.currentText())
        t1 = threading.Thread(target=self.myshow)
        t2 = threading.Thread(target=self.mytr, args=(year, top))
        conn = pymysql.connect(host='localhost', user='root', password='201314xIn', port=3306, db='maoyan',charset='utf8mb4')
        sql = "select * from films"
        db = pd.read_sql(sql, conn)
        db_ = db[(db.year == year)]
        db_ = db_.sort_values(axis=0, ascending=False, by='box_office')
        top_num = 0
        top_ = []
        for index, item in db_.iterrows():
            top_num+=1
            if top_num < (top+1):
                top_.append(item['name'])
        value10 = [965, 847, 582, 555, 550, 462, 366, 360, 282, 273]
        value = value10[0:top]
        word = WordCloud(width=1000)
        word.add("",top_,value,word_size_range = [20,40])
        word.render("wc%d.html"%(year*100+top))
        self.widget.load(QUrl('file:///wc%d.html'%(year*100+top)))
        t1.start()
        t2.start()
        #self.widget.show()
        #word.render("wc%d.png" % (year * 100 + top))

    def click1(self):
        self.form.close()
        Form1 = QtWidgets.QMainWindow()
        self.ui = Mine.Ui_Mine()
        self.ui.setupUi(Form1)
        Form1.show()


    def setupUi(self, Mine2):
        Mine2.setObjectName("Mine2")
        Mine2.resize(1171, 880)
        Mine2.setStyleSheet("border-image: url(:/M16.jpg);")
        Mine2.setWindowFlags(Qt.FramelessWindowHint)
        self.form = Mine2
        self.centralwidget = QtWidgets.QWidget(Mine2)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 330, 1141, 501))
        self.widget.setObjectName("widget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(420, 40, 151, 51))
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("font: 30pt \"隶书\";\n"
"color: rgb(255, 0, 0);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(520, 210, 101, 51))
        self.comboBox_2.setStyleSheet("font: 30pt \"隶书\";\n"
"color: rgb(255, 0, 0);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 40, 72, 51))
        self.label.setStyleSheet("font: 20pt \"幼圆\";\n"
"color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 210, 111, 51))
        self.label_2.setStyleSheet("font: 30pt \"Agency FB\";\n"
"color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(710, 70, 93, 141))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("font: 40pt \"幼圆\";\n"
"color: rgb(255, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(900, 40, 221, 241))
        self.pushButton_2.setStyleSheet("font: 40pt \"幼圆\";\n"
"color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 30, 93, 241))
        self.pushButton_3.setStyleSheet("font: 40pt \"幼圆\";\n"
"color: rgb(255, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        Mine2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Mine2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1171, 26))
        self.menubar.setObjectName("menubar")
        Mine2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Mine2)
        self.statusbar.setObjectName("statusbar")
        Mine2.setStatusBar(self.statusbar)

        self.retranslateUi(Mine2)
        self.pushButton_3.clicked.connect(self.click2)
        self.pushButton.clicked.connect(self.click1)
        self.pushButton_2.clicked.connect(self.click3)
        QtCore.QMetaObject.connectSlotsByName(Mine2)

    def retranslateUi(self, Mine2):
        _translate = QtCore.QCoreApplication.translate
        Mine2.setWindowTitle(_translate("Mine2", "欢迎使用喵眼！"))
        self.comboBox.setItemText(0, _translate("Mine2", "2015"))
        self.comboBox.setItemText(1, _translate("Mine2", "2016"))
        self.comboBox.setItemText(2, _translate("Mine2", "2017"))
        self.comboBox.setItemText(3, _translate("Mine2", "2018"))
        self.comboBox_2.setItemText(0, _translate("Mine2", "3"))
        self.comboBox_2.setItemText(1, _translate("Mine2", "5"))
        self.comboBox_2.setItemText(2, _translate("Mine2", "10"))
        self.label.setText(_translate("Mine2", "年份"))
        self.label_2.setText(_translate("Mine2", "Top"))
        self.pushButton.setText(_translate("Mine2", "返\n"
"回"))
        self.pushButton_2.setText(_translate("Mine2", "不\n"
"  保\n"
"    存"))
        self.pushButton_3.setText(_translate("Mine2", "查\n"
"\n"
"看"))

from PyQt5 import QtWebEngineWidgets
import myqrc_rc
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mine2 = QtWidgets.QMainWindow()  # 注意，这里和我们一开始创建窗体时使用的界面类型相同
    ui = Ui_Mine2()
    ui.setupUi(Mine2)
    Mine2.show()
    sys.exit(app.exec_())