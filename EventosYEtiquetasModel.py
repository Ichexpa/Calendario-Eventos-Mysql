import mysql.connector
class EventosYEtiquetasModelos:
    def __init__(self):
        pass
    def get_evento_y_etiqueta(self,conexionDB,id_evento):
        try:
            conexionDB.conectarse();
            consulta ="""SELECT ev.id_evento, ev.titulo, ev.fecha_hora,
                        ev.duracion, ev.descripcion, ev.importancia, GROUP_CONCAT(et.nombre) AS etiquetas
                        FROM etiquetas_eventos ee INNER JOIN eventos ev ON ee.id_eventos = ev.id_evento
                        INNER JOIN etiquetas et ON ee.id_etiquetas = et.id_etiqueta
                        WHERE ev.id_evento=%s  GROUP BY(ev.id_evento)"""
            conexionDB.ejecutar_consulta(consulta,(id_evento,))
            registro = conexionDB.obtener_registro()
        except mysql.connector.DatabaseError:
            print("Ocurrio un error en la base de datos")
        finally:
            conexionDB.cerrar_conexion()
        return registro

    def get_eventos_por_etiqueta(self,conexionDB,palabra_clave):
        try:
            conexionDB.conectarse()
            consulta = """SELECT DISTINCT ev.id_evento, ev.titulo, ev.fecha_hora,
                        ev.duracion, ev.descripcion, ev.importancia
                        FROM etiquetas_eventos ee INNER JOIN eventos ev ON ee.id_eventos = ev.id_evento
                        INNER JOIN etiquetas et ON ee.id_etiquetas = et.id_etiqueta
                         WHERE et.nombre LIKE %s"""
            conexionDB.ejecutar_consulta(consulta, (f'%{palabra_clave}%',))
            registros = conexionDB.obtener_registros()
        except mysql.connector.DatabaseError:
            print("Ocurrio un error en la base de datos")
        finally:
            conexionDB.cerrar_conexion()
        return registros

