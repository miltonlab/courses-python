def accion():
    print("Activado")
    f = ui.calendario.selectedDate().getDate()
    r = QMessageBox.question(None, "Titulo Mensaje", "Fecha: " + str(f), QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
    

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from quiqt import Ui_MainWindow

import sys
app = QApplication(sys.argv)
win = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(win)
ui.boton.clicked.connect(accion)
win.show()
sys.exit(app.exec_())
