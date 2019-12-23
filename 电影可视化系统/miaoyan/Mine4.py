# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mine4.ui'
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
import pyecharts
from pyecharts import WordCloud
from collections import Counter
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt
from pyecharts_snapshot.main import make_a_snapshot
import threading

class Ui_Mine4(object):

    def myshow(self):
        exec('self.widget.show()')
        exec('self.widget_2.show()')

    def mytr(self,year,top):
        make_a_snapshot("wct%d.html" % (year * 100 + top), ("wct%d.png" % (year * 100 + top)))
        make_a_snapshot("t4%d.html" % (year * 100 + top), ("t4%d.png" % (year * 100 + top)))




    def click3(self):
        year = int(self.comboBox.currentText())
        top = int(self.comboBox_2.currentText())
        try:
            os.remove('wct%d.html' % (year * 100 + top))
            os.remove('t4%d.html' % (year * 100 + top))
            os.remove('wct%d.png' % (year * 100 + top))
            os.remove('t4%d.png' % (year * 100 + top))
        except:
            pass


    def click2(self):
        year = int(self.comboBox.currentText())
        top = int(self.comboBox_2.currentText())
        t1 = threading.Thread(target=self.myshow)
        t2 = threading.Thread(target=self.mytr, args=(year, top))
        conn = pymysql.connect(host='localhost', user='root', password='201314xIn', port=3306, db='maoyan',charset='utf8mb4')
        sql = "select year,actor1,actor2,actor3,actor4 from films"
        db_0 = pd.read_sql(sql, conn)
        db = db_0[(db_0.year == year)]
        dict_ =dict(Counter(db['actor1'].append(db['actor2']).append(db['actor3']).append(db['actor4']).dropna()).most_common(top))
        x = list(dict_.keys())
        y = list(dict_.values())
        top_Bar = pyecharts.Bar(width=500)
        top_Bar.add("",x,y,mark_line=['max'],xaxis_interval = 0,is_labal_show = True)
        top_Bar.render("t4%d.html"%(year*100+top))
        value10 = [965, 847, 582, 555, 550, 462, 366, 360, 282, 273]
        value = value10[0:top]
        word = WordCloud(width=700)
        word.add("",x,value,word_size_range = [20,100])
        word.render("wct%d.html"%(year*100+top))
        self.widget.load(QUrl('file:///wct%d.html' % (year * 100 + top)))
        #self.widget.show()
        self.widget_2.load(QUrl('file:///t4%d.html' % (year * 100 + top)))
        t1.start()
        t2.start()
        #self.widget_2.show()
        #top_Bar.render("t4%d.png" % (year * 100 + top))
        #word.render("wct%d.png" % (year * 100 + top))
    def click1(self):
        self.form.close()
        Form1 = QtWidgets.QMainWindow()
        self.ui = Mine.Ui_Mine()
        self.ui.setupUi(Form1)
        Form1.show()

    def setupUi(self, Mine4):
        Mine4.setObjectName("Mine4")
        Mine4.resize(1347, 790)
        Mine4.setStyleSheet("border-image: url(:/M6.jpg);")
        Mine4.setWindowFlags(Qt.FramelessWindowHint)
        self.form = Mine4
        self.centralwidget = QtWidgets.QWidget(Mine4)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 270, 601, 501))
        self.widget.setObjectName("widget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(360, 0, 151, 51))
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("font: 30pt \"隶书\";\n"
"color: rgb(255, 0, 0);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 0, 72, 51))
        self.label.setStyleSheet("font: 20pt \"隶书\";\n"
"color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 0, 111, 51))
        self.label_2.setStyleSheet("font: 30pt \"Agency FB\";\n"
"color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 0, 71, 111))
        self.pushButton_3.setStyleSheet("font: 20pt \"隶书\";\n"
"color: rgb(255, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 0, 71, 111))
        font = QtGui.QFont()
        font.setFamily("方正舒体")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("font: 20pt \"隶书\";\n"
"color:rgb(255, 0, 0)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 0, 81, 111))
        self.pushButton_2.setStyleSheet("font: 20pt \"隶书\";\n"
"color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(620, 0, 151, 51))
        self.comboBox_2.setStyleSheet("font: 30pt \"隶书\";\n"
"color: rgb(255, 0, 0);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        """
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(850, 30, 171, 181))
        self.label_3.setText("")
        self.gif = QMovie('M14.gif')
        self.label_3.setMovie(self.gif)
        self.gif.start()
        self.label_3.setObjectName("label_3")
        """
        self.widget_2 = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(680, 270, 601, 481))
        self.widget_2.setObjectName("widget_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1090, 20, 191, 181))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gif = QMovie('M20.gif')
        self.label_4.setMovie(self.gif)
        self.gif.start()
        Mine4.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Mine4)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1347, 26))
        self.menubar.setObjectName("menubar")
        Mine4.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Mine4)
        self.statusbar.setObjectName("statusbar")
        Mine4.setStatusBar(self.statusbar)

        self.retranslateUi(Mine4)
        self.pushButton.clicked.connect(self.click1)
        self.pushButton_3.clicked.connect(self.click2)
        self.pushButton_2.clicked.connect(self.click3)
        QtCore.QMetaObject.connectSlotsByName(Mine4)

    def retranslateUi(self, Mine4):
        _translate = QtCore.QCoreApplication.translate
        Mine4.setWindowTitle(_translate("Mine4", "欢迎使用喵眼！"))
        self.comboBox.setItemText(0, _translate("Mine4", "2015"))
        self.comboBox.setItemText(1, _translate("Mine4", "2016"))
        self.comboBox.setItemText(2, _translate("Mine4", "2017"))
        self.comboBox.setItemText(3, _translate("Mine4", "2018"))
        self.label.setText(_translate("Mine4", "年份"))
        self.label_2.setText(_translate("Mine4", "Top"))
        self.pushButton_3.setText(_translate("Mine4", "查\n"
"看"))
        self.pushButton.setText(_translate("Mine4", "返\n"
"回"))
        self.pushButton_2.setText(_translate("Mine4", "不\n"
"保\n"
"存"))
        self.comboBox_2.setItemText(0, _translate("Mine4", "3"))
        self.comboBox_2.setItemText(1, _translate("Mine4", "5"))
        self.comboBox_2.setItemText(2, _translate("Mine4", "10"))

from PyQt5 import QtWebEngineWidgets
import myqrc_rc
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mine4 = QtWidgets.QMainWindow()  # 注意，这里和我们一开始创建窗体时使用的界面类型相同
    ui = Ui_Mine4()
    ui.setupUi(Mine4)
    Mine4.show()
    sys.exit(app.exec_())
