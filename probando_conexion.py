from ConexionDB import ConexionDB;

conexionDB=ConexionDB();
conexionDB.ejecutar_consulta("SELECT * FROM eventos")
resultado= conexionDB.cursor.fetchall()
print(resultado);
conexionDB.cerrar_conexion()