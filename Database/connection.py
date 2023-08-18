import sys
import pyodbc
conn= pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\brein\Documents\VSCode\BaseDeDatos\Basededatos.accdb;")
cursor=conn.cursor()
cursor.execute("SELECT * FROM Persona")
for row in cursor.fetchall():
    print(row)
cursor.close
conn.close