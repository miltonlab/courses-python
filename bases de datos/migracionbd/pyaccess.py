import pyodbc
conex = pyodbc.connect("DRIVER={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\\Users\\usuario\\PycharmProjects\\bds\\BDD_CELICA_CRUZPAMBA (103).accdb")
print("Conexion establecida satisfactoriamente !!!")
cursor = conex.cursor()
cursor.execute("SELECT id, ClaveEdif, Obra, Material, Estado, Area FROM Mejoras")
print("Consulta ejecutada !!!")
print("{0:2} {1:16} {2:26} {3:10} {4:6} {5}".format(
    "ID", "ClaveEdif", "Obra", "Material", "Estado", "Area"
))
registros = cursor.fetchall()
#for registro in cursor:
for registro in registros:
    # print("{0:2} {1:16} {2:16} {3:10} {4:6} {5:.2}".format(registro[0],
    #                                        registro[1],
    #                                        registro[2],
    #                                        registro[3],
    #                                        registro[4],
    #                                        registro[5],))
    print("{0:2} {1:16} {2:16} {3:10} {4:6} {5:.2}".format(
        registro.id, registro.ClaveEdif, registro.Obra,
        registro.Material, registro.Estado, registro.Area)
    )
cursor.close()
conex.close()