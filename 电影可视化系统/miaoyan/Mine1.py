# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mine1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
import Mine
import pyecharts
import pandas as pd
import pymysql
import os
import threading
from PyQt5.QtCore import Qt
from pyecharts_snapshot.main import make_a_snapshot
def visual(a):
    movie = pd.Series(data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],index = ['传记','冒险','剧情','战争','奇幻','家庭','历史','科幻','惊悚','悬疑','爱情','喜剧','犯罪','动画','运动','恐怖','纪录片','其他','动作'])
    for index,item in a.iterrows():
        if (item['type1'] == '传记' or item['type2'] == '传记' or item['type3'] == '传记' or item['type4'] == '传记' or item['type5'] == '传记'):
            movie['传记'] += item['box_office']
        if (item['type1'] == '冒险' or item['type2'] == '冒险' or item['type3'] == '冒险' or item['type4'] == '冒险' or item['type5'] == '冒险'):
            movie['冒险'] += item['box_office']
        if (item['type1'] == '剧情' or item['type2'] == '剧情' or item['type3'] == '剧情' or item['type4'] == '剧情' or item['type5'] == '剧情'):
            movie['剧情'] += item['box_office']
        if (item['type1'] == '战争' or item['type2'] == '战争' or item['type3'] == '战争' or item['type4'] == '战争' or item['type5'] == '战争'):
            movie['战争'] += item['box_office']
        if (item['type1'] == '奇幻' or item['type2'] == '奇幻' or item['type3'] == '奇幻' or item['type4'] == '奇幻' or item['type5'] == '奇幻'):
            movie['奇幻'] += item['box_office']
        if (item['type1'] == '家庭' or item['type2'] == '家庭' or item['type3'] == '家庭' or item['type4'] == '家庭' or item['type5'] == '家庭'):
            movie['家庭'] += item['box_office']
        if (item['type1'] == '历史' or item['type2'] == '历史' or item['type3'] == '历史' or item['type4'] == '历史' or item['type5'] == '历史'):
            movie['历史'] += item['box_office']
        if (item['type1'] == '惊悚' or item['type2'] == '惊悚' or item['type3'] == '惊悚' or item['type4'] == '惊悚' or item['type5'] == '惊悚'):
            movie['惊悚'] += item['box_office']
        if (item['type1'] == '科幻' or item['type2'] == '科幻' or item['type3'] == '科幻' or item['type4'] == '科幻' or item['type5'] == '科幻'):
            movie['科幻'] += item['box_office']
        if (item['type1'] == '悬疑' or item['type2'] == '悬疑' or item['type3'] == '悬疑' or item['type4'] == '悬疑' or item['type5'] == '悬疑'):
            movie['悬疑'] += item['box_office']
        if (item['type1'] == '爱情' or item['type2'] == '爱情' or item['type3'] == '爱情' or item['type4'] == '爱情' or item['type5'] == '爱情'):
            movie['爱情'] += item['box_office']
        if (item['type1'] == '喜剧' or item['type2'] == '喜剧' or item['type3'] == '喜剧' or item['type4'] == '喜剧' or item['type5'] == '喜剧'):
            movie['喜剧'] += item['box_office']
        if (item['type1'] == '动作' or item['type2'] == '动作' or item['type3'] == '动作' or item['type4'] == '动作' or item['type5'] == '动作'):
            movie['动作'] += item['box_office']
        if (item['type1'] == '犯罪' or item['type2'] == '犯罪' or item['type3'] == '犯罪' or item['type4'] == '犯罪' or item['type5'] == '犯罪' or item['type1'] == '警匪' or item['type2'] == '警匪' or item['type3'] == '警匪' or item['type4'] == '警匪' or item['type5'] == '警匪'):
            movie['犯罪'] += item['box_office']
        if (item['type1'] == '动画' or item['type2'] == '动画' or item['type3'] == '动画' or item['type4'] == '动画' or item['type5'] == '动画'):
            movie['动画'] += item['box_office']
        if (item['type1'] == '运动' or item['type2'] == '运动' or item['type3'] == '运动' or item['type4'] == '运动' or item['type5'] == '运动'):
            movie['运动'] += item['box_office']
        if (item['type1'] == '恐怖' or item['type2'] == '恐怖' or item['type3'] == '恐怖' or item['type4'] == '恐怖' or item['type5'] == '恐怖'):
            movie['恐怖'] += item['box_office']
        if (item['type1'] == '纪录片' or item['type2'] == '纪录片' or item['type3'] == '纪录片' or item['type4'] == '纪录片' or item['type5'] == '纪录片'):
            movie['纪录片'] += item['box_office']
        if (item['type1'] == '华语' or item['type2'] == '华语' or item['type3'] == '华语' or item['type4'] == '华语' or item['type5'] == '华语' or item['type1'] == '西部' or item['type2'] == '西部' or item['type3'] == '西部' or item['type4'] == '西部' or item['type5'] == '西部' or item['type1'] == '主题冰雕展' or item['type2'] == '主题冰雕展' or item['type3'] == '主题冰雕展' or item['type4'] == '主题冰雕展' or item['type5'] == '主题冰雕展' or item['type1'] == '音乐' or item['type2'] == '音乐' or item['type3'] == '音乐' or item['type4'] == '音乐' or item['type5'] == '音乐' or item['type1'] == '歌舞' or item['type2'] == '歌舞' or item['type3'] == '歌舞' or item['type4'] == '歌舞' or item['type5'] == '歌舞'):
            movie['其他'] += item['box_office']
    x = list(movie.index)
    y = list(movie.values)
    return x,y

class Ui_Mine1(object):

    def myshow(self):
        exec('self.widget.show()')

    def mytr(self,year,month):
        make_a_snapshot(("db%d.html") % (year * 100 + month),("db%d.png") % (year * 100 + month))



    def click2(self):
        conn = pymysql.connect(host='localhost', user='root', password='201314xIn', port=3306, db='maoyan',charset='utf8mb4')
        sql = "select * from films"
        db = pd.read_sql(sql, conn)
        t1 = threading.Thread(target=self.myshow)
        year = int(self.comboBox.currentText())
        month = int(self.comboBox_2.currentText())
        t2 = threading.Thread(target=self.mytr,args = (year,month))
        if month < 13:
            db_ = db[(db.year == year) & (db.month == month)]
        elif month > 123:
            db_= db[(db.year == year)&(db.month>0)&(db.month<4)]
        elif month == 456:
            db_ = db[(db.year == year) & (db.month > 3) & (db.month < 7)]
        elif month == 789:
            db_ = db[(db.year == year) & (db.month > 6) & (db.month < 10)]
        elif month == 101112:
            db_ = db[(db.year == year) & (db.month > 9) & (db.month < 13)]
        else:
            db_ = db
        x, y = visual(db_)
        pie = pyecharts.Pie()
        pie.add("", x, y, is_label_show=True, radius=[0, 50], center=[75, 50],legend_orient="vertical", legend_pos="right")
        bar = pyecharts.Bar("", title_pos="left")
        bar.add("", x, y, mark_line=["max", "average"], xaxis_interval=0,is_labal_show=True)
        grid = pyecharts.Grid(width=1200)
        grid.add(bar, grid_right='50%')
        grid.add(pie, grid_left="50%")
        grid.render(("db%d.html")%(year*100+month))
        self.widget.load(QUrl('file:///db%d.html'%(year*100+month)))
        t1.start()
        t2.start()
        #self.widget.show()
        #grid.render(("db%d.png") % (year * 100 + month))

    def click3(self):
        year = int(self.comboBox.currentText())
        month = int(self.comboBox_2.currentText())
        try:
            os.remove('db%d.html'%(year*100+month))
            os.remove('db%d.png'%(year*100+month))
        except:
            pass


    def click1(self):
        self.form.close()
        Form1 = QtWidgets.QMainWindow()
        self.ui = Mine.Ui_Mine()
        self.ui.setupUi(Form1)
        Form1.show()


    def setupUi(self, Mine1):
        Mine1.setObjectName("Mine1")
        Mine1.resize(1400, 833)
        Mine1.setStyleSheet("border-image: url(:/M8.png);")
        Mine1.setWindowFlags(Qt.FramelessWindowHint)
        self.form = Mine1
        self.centralwidget = QtWidgets.QWidget(Mine1)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(450, 70, 91, 31))
        self.comboBox.setStyleSheet("border-image: url(:/button3.png);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(740, 70, 91, 31))
        self.comboBox_2.setStyleSheet("border-image: url(:/button3.png);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 70, 91, 31))
        self.label_2.setStyleSheet("font: 10pt \"幼圆\";\n"
"color: rgb(85, 170, 255);""border-image: url(:/M9.png);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(650, 70, 91, 31))
        self.label_3.setStyleSheet("font: 10pt \"幼圆\";\n"
"color: rgb(85, 170, 255);""border-image: url(:/M9.png);")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1140, 70, 93, 31))
        self.pushButton.setStyleSheet("font: 20pt \"幼圆\";\n"
"color: rgb(85, 170, 255);""border-image: url(:/M9.png);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(940, 70, 93, 31))
        self.pushButton_3.setStyleSheet("font: 20pt \"幼圆\";\n"
"color: rgb(85, 170, 255);""border-image: url(:/M9.png);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 70, 91, 31))
        self.pushButton_2.setStyleSheet("font: 20pt \"幼圆\";\n"
"color: rgb(85, 170, 255);""border-image: url(:/M9.png);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(110, 130, 1191, 611))
        self.widget.setObjectName("widget")
        Mine1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Mine1)
        self.statusbar.setObjectName("statusbar")
        Mine1.setStatusBar(self.statusbar)

        self.retranslateUi(Mine1)
        self.pushButton.clicked.connect(self.click3)
        self.pushButton_2.clicked.connect(self.click1)
        self.pushButton_3.clicked.connect(self.click2)
        QtCore.QMetaObject.connectSlotsByName(Mine1)

    def retranslateUi(self, Mine1):
        _translate = QtCore.QCoreApplication.translate
        Mine1.setWindowTitle(_translate("Mine1", "欢迎使用喵眼！"))
        self.comboBox.setItemText(0, _translate("Mine1", "2015"))
        self.comboBox.setItemText(1, _translate("Mine1", "2016"))
        self.comboBox.setItemText(2, _translate("Mine1", "2017"))
        self.comboBox.setItemText(3, _translate("Mine1", "2018"))
        self.comboBox_2.setItemText(0, _translate("Mine1", "1"))
        self.comboBox_2.setItemText(1, _translate("Mine1", "1"))
        self.comboBox_2.setItemText(2, _translate("Mine1", "2"))
        self.comboBox_2.setItemText(3, _translate("Mine1", "3"))
        self.comboBox_2.setItemText(4, _translate("Mine1", "4"))
        self.comboBox_2.setItemText(5, _translate("Mine1", "5"))
        self.comboBox_2.setItemText(6, _translate("Mine1", "6"))
        self.comboBox_2.setItemText(7, _translate("Mine1", "7"))
        self.comboBox_2.setItemText(8, _translate("Mine1", "8"))
        self.comboBox_2.setItemText(9, _translate("Mine1", "9"))
        self.comboBox_2.setItemText(10, _translate("Mine1", "10"))
        self.comboBox_2.setItemText(11, _translate("Mine1", "11"))
        self.comboBox_2.setItemText(12, _translate("Mine1", "12"))
        self.comboBox_2.setItemText(13, _translate("Mine1", "123"))
        self.comboBox_2.setItemText(14, _translate("Mine1", "456"))
        self.comboBox_2.setItemText(15, _translate("Mine1", "789"))
        self.comboBox_2.setItemText(16, _translate("Mine1", "101112"))
        self.label_2.setText(_translate("Mine1", " 年     份"))
        self.label_3.setText(_translate("Mine1", " 月份/季度"))
        self.pushButton.setText(_translate("Mine1", "删除"))
        self.pushButton_3.setText(_translate("Mine1", "查看"))
        self.pushButton_2.setText(_translate("Mine1", "返回"))

from PyQt5 import QtWebEngineWidgets
import myqrc_rc
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mine1 = QtWidgets.QMainWindow()  # 注意，这里和我们一开始创建窗体时使用的界面类型相同
    ui = Ui_Mine1()
    ui.setupUi(Mine1)
    Mine1.show()
    sys.exit(app.exec_())
