
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

from catastromio import Ui_catastromio
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtq
import PyQt5.QtCore as qtc
import sys
import sqlite3

class VentanaPropietarios(qtw.QMainWindow):
    def __init__(self):
        qtw.QMainWindow.__init__(self)
        self.ui = Ui_catastromio()
        """
        Esto es para enlazar la interfaz grafica diseñada en QT Creator (xml)
        con mi objeto Py Local "Ventana"
        """
        self.ui.setupUi(self)
        self.ui.b_guardar.clicked.connect(self.insertar)
        self.ui.actualizar.clicked.connect(self.actualiza)
        self.con = sqlite3.connect("celica.db")

 ##       self.ui.calcula.clicked.connect(self.calcular)

    def insertar(self):
        cedula = self.ui.le_cedula.text()
        nombres = self.ui.le_nombres.text()
        apellidos = self.ui.le_apellidos.text()
        try:
            cursor = self.con.execute("INSERT INTO propietarios VALUES (?, ?, ?)", (cedula, nombres, apellidos))
            self.con.commit()
            QMessageBox.information(self, "Aplcation Catast::", "Proietario guardado exitosamente. ")
            cursor.close()

        except Exception as ex:
            print("ERROR AL GRABAR LOS DATOS DE PROPIETARIO", ex)

    def actualiza(self):
        cursor = self.con.cursor()
        cursor.execute("SELECT clave_catastral, nombres, apellidos FROM propietarios")
        propietarios = cursor.fetchall()

        self.ui.tablaver.setColumnCount(3)   # Para definir cuantas columnas ha de tener nuestro TableView
        self.ui.tablaver.setRowCount(len(propietarios))     # Para Extraer el número de registro de la variable propietarios

        fila = 0

        try:
            for persona in propietarios:
                celdaCedula = QTableWidgetItem(persona[0])
                self.ui.tablaver.setItem(fila, 0, celdaCedula)
                celdaNombres = QTableWidgetItem(persona[1])
                self.ui.tablaver.setItem(fila, 1, celdaNombres)
                celdaApellidos = QTableWidgetItem(persona[2])
                self.ui.tablaver.setItem(fila, 2, celdaApellidos)
                fila = fila + 1

        except Exception as ex:
            print("ERROR AL GRABAR LOS DATOS DE PROPIETARIO", ex)



##        print("Activado")
##        qtw.QMessageBox.about(self, "Mensaje", "Activado")

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    Ventana = VentanaPropietarios()
    ##ui = Ui_VentanaAreas()
    Ventana.show()
    sys.exit(app.exec_())

