import sys

# import sqlite3
import PyQt5.QtSql as qtsql
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc

#from qtw import QMessageBox, QTableWidgetItem


from catastromio import Ui_catastromio


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
        self.ui.eliminar.clicked.connect(self.elimina)
        try:
            # Cargar el driver QtQSQL para Sqlite
            dbsqlite3 = qtsql.QSqlDatabase.addDatabase('QSQLITE')
            # Cargar la BD
            dbsqlite3.setDatabaseName('Celica.db')
            if not dbsqlite3.open():
                qtw.QMessageBox.error(self, "App Catastro",
                                      "No se puede conectar a la BD. ")
            else:
                print("conexion establecida !!!")
        except Exception as ex:
            qtw.QMessageBox.error(self, "App Catastro",
                                 "Error: " + str(ex))
        self.modelo = ModeloTablaSql()
        self.ui.tablaver.setModel(self.modelo)

    def insertar(self):
        cedula = self.ui.le_cedula.text()
        nombres = self.ui.le_nombres.text()
        apellidos = self.ui.le_apellidos.text()
        try:
            cursor = self.con.execute("INSERT INTO propietarios VALUES (?, ?, ?)", (cedula, nombres, apellidos))
            self.con.commit()
            qtw.QMessageBox.information(self, "Aplcation Catast::", "Proietario guardado exitosamente. ")
            cursor.close()

        except Exception as ex:
            print("ERROR AL GRABAR LOS DATOS DE PROPIETARIO", ex)

    def actualiza(self):
        # Insertar un nuevo registro en el TableView
        self.modelo.insertar()

    def elimina(self):
        self.modelo.removeRow(
            self.ui.tablaver.currentIndex().row())

class ModeloTablaSql(qtsql.QSqlTableModel):
    def __init__(self):
        qtsql.QSqlTableModel.__init__(self)
        print("construyendo modelo")
        # Se fija la tabla de la base de datos
        self.setTable("propietarios")
        self.setHeaderData(0, qtc.Qt.Horizontal, "CLAVE CATASTRAL")
        self.setHeaderData(1, qtc.Qt.Horizontal, "NOMBRES")
        self.setHeaderData(2, qtc.Qt.Horizontal, "APELLIDOS")
        self.setEditStrategy(qtsql.QSqlTableModel.OnFieldChange)
        self.select()

    def insertar(self):
        try:
            num_filas = self.rowCount()
            self.insertRows(num_filas, 1)
            self.index(num_filas + 1, 1)
        except Exception as ex:
            print("Error: " , str(ex))


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    Ventana = VentanaPropietarios()
    ##ui = Ui_VentanaAreas()
    Ventana.show()
    sys.exit(app.exec_())

