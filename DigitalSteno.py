# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DigitalSteno.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(246, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn1.setIconSize(QtCore.QSize(16, 16))
        self.btn1.setObjectName("btn1")
        self.horizontalLayout.addWidget(self.btn1)
        self.NameFile = QtWidgets.QLineEdit(self.centralwidget)
        self.NameFile.setText("")
        self.NameFile.setReadOnly(True)
        self.NameFile.setPlaceholderText("")
        self.NameFile.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.NameFile.setObjectName("NameFile")
        self.horizontalLayout.addWidget(self.NameFile)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setObjectName("btn2")
        self.verticalLayout.addWidget(self.btn2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setObjectName("btn3")
        self.horizontalLayout_2.addWidget(self.btn3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DigitalSteno"))
        self.btn1.setText(_translate("MainWindow", "Выбрать видеофайл"))
        self.btn2.setText(_translate("MainWindow", "Принять Результат"))
        self.btn3.setText(_translate("MainWindow", "Добавить в словарь"))

