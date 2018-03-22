# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\guiqt.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hora = QtWidgets.QTimeEdit(self.centralwidget)
        self.hora.setGeometry(QtCore.QRect(170, 50, 118, 22))
        self.hora.setObjectName("hora")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 50, 47, 13))
        self.label.setObjectName("label")
        self.calendario = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendario.setGeometry(QtCore.QRect(80, 120, 312, 183))
        self.calendario.setObjectName("calendario")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 47, 13))
        self.label_2.setObjectName("label_2")
        self.boton = QtWidgets.QPushButton(self.centralwidget)
        self.boton.setGeometry(QtCore.QRect(320, 330, 75, 23))
        self.boton.setObjectName("boton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuEjemplo_de_Qt = QtWidgets.QMenu(self.menubar)
        self.menuEjemplo_de_Qt.setObjectName("menuEjemplo_de_Qt")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuEjemplo_de_Qt.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "HORA:"))
        self.label_2.setText(_translate("MainWindow", "FECHA:"))
        self.boton.setText(_translate("MainWindow", "ACCION"))
        self.menuEjemplo_de_Qt.setTitle(_translate("MainWindow", "Ejemplo de Qt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

