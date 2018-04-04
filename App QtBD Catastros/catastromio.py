# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'catastromio.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_catastromio(object):
    def setupUi(self, catastromio):
        catastromio.setObjectName("catastromio")
        catastromio.resize(400, 559)
        self.centralWidget = QtWidgets.QWidget(catastromio)
        self.centralWidget.setObjectName("centralWidget")
        self.le_cedula = QtWidgets.QLineEdit(self.centralWidget)
        self.le_cedula.setGeometry(QtCore.QRect(130, 37, 113, 20))
        self.le_cedula.setObjectName("le_cedula")
        self.le_nombres = QtWidgets.QLineEdit(self.centralWidget)
        self.le_nombres.setGeometry(QtCore.QRect(130, 67, 231, 20))
        self.le_nombres.setObjectName("le_nombres")
        self.le_apellidos = QtWidgets.QLineEdit(self.centralWidget)
        self.le_apellidos.setGeometry(QtCore.QRect(130, 97, 231, 20))
        self.le_apellidos.setObjectName("le_apellidos")
        self.b_guardar = QtWidgets.QPushButton(self.centralWidget)
        self.b_guardar.setGeometry(QtCore.QRect(120, 130, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.b_guardar.setFont(font)
        self.b_guardar.setObjectName("b_guardar")
        self.b_limpiar = QtWidgets.QPushButton(self.centralWidget)
        self.b_limpiar.setGeometry(QtCore.QRect(220, 130, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.b_limpiar.setFont(font)
        self.b_limpiar.setObjectName("b_limpiar")
        self.lb_cedula = QtWidgets.QLabel(self.centralWidget)
        self.lb_cedula.setGeometry(QtCore.QRect(50, 39, 71, 21))
        self.lb_cedula.setObjectName("lb_cedula")
        self.lb_nombres = QtWidgets.QLabel(self.centralWidget)
        self.lb_nombres.setGeometry(QtCore.QRect(50, 70, 71, 20))
        self.lb_nombres.setObjectName("lb_nombres")
        self.lb_apellidos = QtWidgets.QLabel(self.centralWidget)
        self.lb_apellidos.setGeometry(QtCore.QRect(50, 100, 71, 20))
        self.lb_apellidos.setObjectName("lb_apellidos")
        self.vent_titulo = QtWidgets.QLabel(self.centralWidget)
        self.vent_titulo.setGeometry(QtCore.QRect(30, 0, 631, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.vent_titulo.setFont(font)
        self.vent_titulo.setObjectName("vent_titulo")
        self.tablaver = QtWidgets.QTableView(self.centralWidget) ### Trampa para que reconozca el Python
        #self.tablaver = QtWidgets.QTableWidget(self.centralWidget)
        self.tablaver.setGeometry(QtCore.QRect(25, 160, 451, 251))
        self.tablaver.setObjectName("tablaver")
        self.actualizar = QtWidgets.QPushButton(self.centralWidget)
        self.actualizar.setGeometry(QtCore.QRect(30, 420, 101, 23))
        self.eliminar = QtWidgets.QPushButton(self.centralWidget)
        self.eliminar.setGeometry(QtCore.QRect(140, 420, 101, 23))

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actualizar.setFont(font)
        self.actualizar.setObjectName("actualizar")
        self.eliminar.setFont(font)
        self.eliminar.setObjectName("eliminar")

        catastromio.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(catastromio)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menuBar.setObjectName("menuBar")
        catastromio.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(catastromio)
        self.mainToolBar.setObjectName("mainToolBar")
        catastromio.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(catastromio)
        self.statusBar.setObjectName("statusBar")
        catastromio.setStatusBar(self.statusBar)

        self.retranslateUi(catastromio)
        QtCore.QMetaObject.connectSlotsByName(catastromio)

    def retranslateUi(self, catastromio):
        _translate = QtCore.QCoreApplication.translate
        catastromio.setWindowTitle(_translate("catastromio", "Gestion de Propietarios"))
        self.b_guardar.setText(_translate("catastromio", "GUARDAR"))
        self.b_limpiar.setText(_translate("catastromio", "LIMPIAR"))
        self.lb_cedula.setText(_translate("catastromio", "CEDULA:"))
        self.lb_nombres.setText(_translate("catastromio", "NOMBRES:"))
        self.lb_apellidos.setText(_translate("catastromio", "APELLIDOS:"))
        self.vent_titulo.setText(_translate("catastromio", "Ingreso de Datos Personales"))
        self.actualizar.setText(_translate("catastromio", "INSERTAR"))
        self.eliminar.setText(_translate("catastromio", "ELIMINAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    catastromio = QtWidgets.QMainWindow()
    ui = Ui_catastromio()
    ui.setupUi(catastromio)
    catastromio.show()
    sys.exit(app.exec_())

