import pyodbc

con = pyodbc.connect("DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Users\\usuario\\Documents\\ml\\BDD_CELICA_CRUZPAMBA (103).accdb")
cur = con.cursor()
for table in cur.tables(tableType='TABLE'):
    print(table.table_name)

cur.execute("select id, Clave_predio from Viviendas")
filas = cur.fetchall()
for f in filas:
    print(f.id)
    print(f.Clave_predio)
