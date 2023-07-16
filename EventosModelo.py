import mysql.connector
from datetime import date, datetime, timedelta, time
from calendar import monthrange

class EventosModelo:
    def __init__(self):
        pass
    def get_eventos(self,conexionDB):
        try:
            conexionDB.conectarse();
            consulta = """SELECT id_evento,titulo,fecha_hora,duracion,descripcion,importancia FROM eventos ORDER BY fecha_hora"""
            conexionDB.ejecutar_consulta(consulta);
            registros=conexionDB.obtener_registros();
        except mysql.connector.DatabaseError:
            print("Ocurrio un error en la base de datos")
        finally:
            conexionDB.cerrar_conexion()
        return registros;

    def get_eventos_semanales(self, conexionDB,dias):
        fechaActual = datetime.now().date()
        fechaLimiteSuperior = fechaActual+timedelta(days=dias)
        fechaLimiteInferior = fechaLimiteSuperior-timedelta(days=7)
        try:
            conexionDB.conectarse()
            consulta = f"SELECT * FROM calendario_eventos.eventos WHERE fecha_hora BETWEEN '{fechaLimiteInferior}' AND '{fechaLimiteSuperior}'"
            conexionDB.ejecutar_consulta(consulta)
            registros = conexionDB.obtener_registros()
        except mysql.connector.DatabaseError:
            print("Ocurrio un error en la base de datos")
        finally:
            conexionDB.cerrar_conexion()
        return registros;
        print(type(str(fechaLimiteSuperior)))
        print(fechaLimiteInferior)
        
""" a=EventosModelo();
print(a.get_eventos_semanales(7)) """
