"""
Problema: Migrar los datos de la BD de Acsess a una nueva BD en Sqlite
Caso concreto de migracion: Migrar los datos de la Tabla PREDIOS
(Clave, Nombres, Apellidos) a la tabla llamada PROPIETARIO en la nueva
BD.
"""
import pyodbc
import sqlite3

dbaccess = pyodbc.connect("DRIVER={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\\Users\\usuario\\PycharmProjects\\bds\\BDD_CELICA_CRUZPAMBA (103).accdb")

dbsqlite = sqlite3.connect("C:\\Users\\usuario\\PycharmProjects\\bds\\Celica.db")
cursor1 = dbaccess.cursor()
cursor2 = dbsqlite.cursor()
cursor1.execute("SELECT Clave, Propietario_Nombres, Propietario_apellidos FROM Predios")
#cursor1.execute("SELECT * FROM Predios")
predios = cursor1.fetchall()
for predio in predios:
    #print(predio)
    cursor2.execute("INSERT INTO Propietarios VALUES ('{0}','{1}','{2}')".format(
        predio.Clave, predio.Propietario_Nombres, predio.Propietario_apellidos
    ))
dbsqlite.commit()
cursor1.close()
cursor2.close()
dbaccess.close()
dbsqlite.close()



