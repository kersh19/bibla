# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sa.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(229, 208)
        Form.setMinimumSize(QtCore.QSize(229, 208))
        Form.setMaximumSize(QtCore.QSize(229, 208))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 231, 211))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setPixmap(QtGui.QPixmap("img/kek.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 231, 211))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(40, 0, 40, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 0, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_3.addWidget(self.pushButton_6, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Меню"))
        self.pushButton_5.setText(_translate("Form", "Каталог книг"))
        self.pushButton_6.setText(_translate("Form", "Читательский билет"))
#import img_rc


