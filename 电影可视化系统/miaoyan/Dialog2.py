# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog2(object):
    def setupUi(self, Dialog2):
        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(293, 341)
        Dialog2.setStyleSheet("border-image: url(:/button3.png);\n"
"font: 20pt \"方正舒体\";")
        self.form = Dialog2
        self.label = QtWidgets.QLabel(Dialog2)
        self.label.setGeometry(QtCore.QRect(0, -10, 291, 271))
        self.label.setStyleSheet("font: 20pt \"方正姚体\";\n"
"border-image: url(:/bug.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog2)
        self.pushButton.setGeometry(QtCore.QRect(0, 260, 291, 81))
        self.pushButton.setStyleSheet("border-image: url(:/background2.png);\n"
"font: 20pt \"华文彩云\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setAutoRepeatDelay(300)
        self.pushButton.setAutoRepeatInterval(100)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog2)
        self.pushButton.clicked.connect(Dialog2.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2):
        _translate = QtCore.QCoreApplication.translate
        Dialog2.setWindowTitle(_translate("Dialog2", "欢迎使用喵眼！"))
        self.pushButton.setText(_translate("Dialog2", "确认"))

import myqrc_rc
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog2 = QtWidgets.QDialog()  # 注意，这里和我们一开始创建窗体时使用的界面类型相同
    ui = Ui_Dialog2()
    ui.setupUi(Dialog2)
    Dialog2.show()
    sys.exit(app.exec_())