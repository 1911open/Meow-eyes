# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mine5.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from qtpandas.models.DataFrameModel import DataFrameModel
import pymysql
import pandas as pd
conn = pymysql.connect(host='localhost', user='root', password='201314xIn', port=3306, db='maoyan',charset='utf8mb4')
sql = "select * from films"
db = pd.read_sql(sql, conn)
db = db
from PyQt5.QtCore import Qt
import Mine
class Ui_Mine5(object):
    def click1(self):
        self.form.close()
        Form1 = QtWidgets.QMainWindow()
        self.ui = Mine.Ui_Mine()
        self.ui.setupUi(Form1)
        Form1.show()

    def setupUi(self, Mine5):
        Mine5.setObjectName("Mine5")
        Mine5.resize(1259, 879)
        Mine5.setStyleSheet("border-image: url(:/M11.jpg);")
        Mine5.setWindowFlags(Qt.FramelessWindowHint)
        self.form = Mine5
        self.centralwidget = QtWidgets.QWidget(Mine5)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, -10, 861, 101))
        self.pushButton.setStyleSheet("border-image: url(:/M16.jpg);\n"
"font: 14pt \"华文新魏\";")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(890, 0, 361, 81))
        self.label_2.setStyleSheet("\n"
"border-image: url(:/M10.jpg);")
        self.label_2.setObjectName("label_2")
        self.pandastablewidget = DataTableWidget(self.centralwidget)
        self.pandastablewidget.setGeometry(QtCore.QRect(-10, 90, 1251, 741))
        self.pandastablewidget.setStyleSheet("border-image: url(:/M8.png);")
        self.pandastablewidget.setObjectName("pandastablewidget")
        self.model = DataFrameModel()
        self.pandastablewidget.setViewModel(self.model)
        self.model.setDataFrame(db)
        Mine5.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Mine5)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1259, 26))
        self.menubar.setObjectName("menubar")
        Mine5.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Mine5)
        self.statusbar.setObjectName("statusbar")
        Mine5.setStatusBar(self.statusbar)

        self.retranslateUi(Mine5)
        self.pushButton.clicked.connect(self.click1)
        QtCore.QMetaObject.connectSlotsByName(Mine5)

    def retranslateUi(self, Mine5):
        _translate = QtCore.QCoreApplication.translate
        Mine5.setWindowTitle(_translate("Mine5", "欢迎使用喵眼！"))
        self.pushButton.setText(_translate("Mine5", "返回"))
        self.label_2.setText(_translate("Mine5", "TextLabel"))

from qtpandas.views.DataTableView import DataTableWidget
import myqrc_rc
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mine5 = QtWidgets.QMainWindow()  # 注意，这里和我们一开始创建窗体时使用的界面类型相同
    ui = Ui_Mine5()
    ui.setupUi(Mine5)
    Mine5.show()
    sys.exit(app.exec_())
