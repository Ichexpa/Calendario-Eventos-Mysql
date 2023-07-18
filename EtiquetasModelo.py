import mysql.connector
from datetime import date, datetime, timedelta, time
from calendar import monthrange
from ConexionDB import ConexionDB
class EtiquetasModelo:
    def __init__(self):
        pass
    def ingresar_etiquetas(self,conexionDB,etiqueta):
        try:            
            conexionDB.conectarse();
            consulta="INSERT INTO etiquetas(nombre) VALUE(%s)"
            conexionDB.ejecutar_consulta(consulta,(etiqueta,))
            conexionDB.aplicar_cambios()
            id_generado = conexionDB.obtener_id_registro_creado();
        except mysql.connector.Error as cod_error:
            print(f"Codigo de error {cod_error.errno}")
            if(cod_error.errno==1062):
                id_generado = self.get_id_etiqueta(conexionDB, etiqueta)[0]
        finally:
            conexionDB.cerrar_conexion()

        return id_generado
    def get_id_etiqueta(self,conexionDB,etiqueta):
        try:
            conexionDB.conectarse()
            consulta = "SELECT id_etiqueta FROM etiquetas WHERE nombre=%s"
            conexionDB.ejecutar_consulta(consulta, (etiqueta,))
            id_etiqueta= conexionDB.obtener_registro()
        except mysql.connector.Error as cod_error:
            print(f"Codigo de error {cod_error.errno}")
            return None;
        finally:
            conexionDB.cerrar_conexion()
        return id_etiqueta;

""" consulta=EtiquetasModelo()
conexionDB = ConexionDB()
print(consulta.ingresar_etiquetas(conexionDB,"Comida")) """
