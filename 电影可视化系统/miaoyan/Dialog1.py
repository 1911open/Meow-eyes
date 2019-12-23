# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog1(object):
    def setupUi(self, Dialog1):
        Dialog1.setObjectName("Dialog1")
        Dialog1.resize(271, 320)
        self.form = Dialog1
        self.label = QtWidgets.QLabel(Dialog1)
        self.label.setGeometry(QtCore.QRect(0, 0, 271, 251))
        self.label.setStyleSheet("font: 20pt \"黑体\";\n"
"border-image: url(:/button3.png);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog1)
        self.pushButton.setGeometry(QtCore.QRect(0, 250, 271, 71))
        self.pushButton.setStyleSheet("border-image: url(:/background2.png);\n"
"font: 20pt \"华文彩云\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setAutoRepeatDelay(300)
        self.pushButton.setAutoRepeatInterval(100)
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Dialog1)
        self.pushButton.clicked.connect(Dialog1.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog1)

    def retranslateUi(self, Dialog1):
        _translate = QtCore.QCoreApplication.translate
        Dialog1.setWindowTitle(_translate("Dialog1", "欢迎使用喵眼！"))
        self.label.setText(_translate("Dialog1", "TextLabel"))
        self.pushButton.setText(_translate("Dialog1", "确认"))

import myqrc_rc
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    page1_1 = QtWidgets.QDialog()  # 注意，这里和我们一开始创建窗体时使用的界面类型相同
    ui = Ui_Dialog1()
    ui.setupUi(page1_1)
    page1_1.show()
    sys.exit(app.exec_())
