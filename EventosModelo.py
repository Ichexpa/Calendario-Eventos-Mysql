import mysql.connector
from datetime import date, datetime, timedelta, time
from calendar import monthrange

from AdministradorDeFechas import AdministradorDeFechas

class EventosModelo:
    def __init__(self):
        pass
    def get_eventos(self,conexionDB):
        try:
            conexionDB.conectarse();
            consulta = """SELECT id_evento,titulo,fecha_hora,duracion,descripcion,importancia 
                            FROM eventos ORDER BY fecha_hora"""
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
            consulta = f"""SELECT id_evento,titulo,fecha_hora,duracion,descripcion,importancia
                        FROM eventos WHERE fecha_hora BETWEEN 
                        '{fechaLimiteInferior}' AND '{fechaLimiteSuperior}'"""
            conexionDB.ejecutar_consulta(consulta)
            registros = conexionDB.obtener_registros()
        except mysql.connector.DatabaseError:
            print("Ocurrio un error en la base de datos")
        finally:
            conexionDB.cerrar_conexion()
        return registros;
        print(type(str(fechaLimiteSuperior)))
        print(fechaLimiteInferior)
    def eliminar_evento(self,conexionDB,id):
        try:
            conexionDB.conectarse();
            consulta="""DELETE FROM eventos WHERE id_evento=%s"""
            conexionDB.ejecutar_consulta(consulta,(id,));
            conexionDB.aplicar_cambios()
        except mysql.connector.DatabaseError:
            print("Ocurrio un error en la base de datos")
        finally:
            conexionDB.cerrar_conexion()        
    
    def crear_evento(self,conexionDB,evento):
        try:
            conexionDB.conectarse()
            consulta = """INSERT INTO eventos(titulo,fecha_hora,duracion,importancia,descripcion)
                             VALUES(%s,%s,%s,%s,%s)"""
            fechaTipoDateTime = AdministradorDeFechas.unirFechaYHoraCadenasEnDatetime(
                evento.fecha, evento.hora)
            print(fechaTipoDateTime)
            info_evento = (evento.titulo, fechaTipoDateTime, evento.duracion, evento.importancia,evento.descripcion)
            conexionDB.ejecutar_consulta(consulta,info_evento)
            conexionDB.aplicar_cambios()
            id_generado=conexionDB.obtener_id_registro_creado();
        except mysql.connector.DatabaseError:
            raise mysql.connector.IntegrityError
        finally:
            conexionDB.cerrar_conexion()
        print(id_generado)
        return id_generado;

    def editar_evento(self, conexionDB, evento):
        try:
            conexionDB.conectarse()
            consulta = """UPDATE eventos SET titulo=%s,fecha_hora=%s,duracion=%s,importancia=%s,descripcion=%s
                             WHERE id_evento=%s"""
            fechaTipoDateTime = AdministradorDeFechas.unirFechaYHoraCadenasEnDatetime(
                evento.fecha, evento.hora)
            print(fechaTipoDateTime)
            info_evento = (evento.titulo, fechaTipoDateTime,
                           evento.duracion, evento.importancia, evento.descripcion, evento.id)
            conexionDB.ejecutar_consulta(consulta, info_evento)
            conexionDB.aplicar_cambios()
        except mysql.connector.DatabaseError:
            raise mysql.connector.IntegrityError
        finally:
            conexionDB.cerrar_conexion()

    def get_eventos_mensuales(self, conexionDB,mes_inf,mes_sup):
        try:
            conexionDB.conectarse()
            consulta = f"""SELECT id_evento,titulo,fecha_hora,duracion,descripcion,importancia
                        FROM eventos WHERE fecha_hora BETWEEN 
                        '{mes_inf}' AND '{mes_sup}'"""
            conexionDB.ejecutar_consulta(consulta)
            registros = conexionDB.obtener_registros()
        except mysql.connector.DatabaseError:
            print("Ocurrio un error en la base de datos")
        finally:
            conexionDB.cerrar_conexion()
        return registros
