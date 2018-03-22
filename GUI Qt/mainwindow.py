# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.textRadianes = QtWidgets.QLineEdit(self.centralWidget)
        self.textRadianes.setGeometry(QtCore.QRect(170, 80, 113, 20))
        self.textRadianes.setObjectName("textRadianes")
        self.labelRadianes = QtWidgets.QLabel(self.centralWidget)
        self.labelRadianes.setGeometry(QtCore.QRect(90, 80, 47, 13))
        self.labelRadianes.setObjectName("labelRadianes")
        self.labelGrados = QtWidgets.QLabel(self.centralWidget)
        self.labelGrados.setGeometry(QtCore.QRect(190, 130, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelGrados.setFont(font)
        self.labelGrados.setObjectName("labelGrados")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelRadianes.setText(_translate("MainWindow", " Radianes:"))
        self.labelGrados.setText(_translate("MainWindow", "Grados"))

