import mysql.connector
from EventosModelo import EventosModelo;
from EtiquetasModelo import EtiquetasModelo;
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

    def ingresar_eventos_por_etiqueta(self,conexionDB,evento):
        try:
            evento_modelo=EventosModelo()
            etiqueta_modelo=EtiquetasModelo()
            consulta = """INSERT INTO etiquetas_eventos(id_eventos,id_etiquetas)
                            VALUES(%s,%s)"""
            id_evento_creado=evento_modelo.crear_evento(conexionDB,evento);
            etiquetas_de_evento = evento.identificadorEvento.split(",");
            print(etiquetas_de_evento)
            for etiqueta in etiquetas_de_evento:
                etiqueta_sin_espacios=etiqueta.strip();
                print(etiqueta_sin_espacios)
                id_etiqueta_creada=etiqueta_modelo.ingresar_etiquetas(conexionDB,etiqueta_sin_espacios);
                print(id_etiqueta_creada)
                conexionDB.conectarse()
                conexionDB.ejecutar_consulta(consulta,(id_evento_creado,id_etiqueta_creada))
                conexionDB.aplicar_cambios()
                conexionDB.cerrar_conexion();
        except mysql.connector.IntegrityError:
            print("Registro con fecha Duplicada")
            return False; 
        except mysql.connector.Error as e:
            print(f"Codigo de error numero {e.errno}")
            return False
        finally:
            conexionDB.cerrar_conexion()
        return True,id_evento_creado

    def editar_eventos_por_etiqueta(self, conexionDB, evento):
        try:
            evento_modelo = EventosModelo()
            etiqueta_modelo = EtiquetasModelo()
            
            consulta = """INSERT INTO etiquetas_eventos(id_eventos,id_etiquetas)
                            VALUES(%s,%s)"""
            evento_modelo.editar_evento(conexionDB, evento)
            conjunto_de_id_etiquetas = []
            etiquetas_de_evento = evento.identificadorEvento.split(",")
            print(etiquetas_de_evento)
            for etiqueta in etiquetas_de_evento:
                etiqueta_sin_espacios = etiqueta.strip()
                print(etiqueta_sin_espacios)
                id_etiqueta_creada = etiqueta_modelo.ingresar_etiquetas(
                    conexionDB, etiqueta_sin_espacios)
                conjunto_de_id_etiquetas.append(id_etiqueta_creada)
                if(self.etiqueta_relacionada_a_evento(conexionDB,evento.id,id_etiqueta_creada)):
                    
                    conexionDB.conectarse()
                    conexionDB.ejecutar_consulta(
                        consulta, (evento.id, id_etiqueta_creada))
                    conexionDB.aplicar_cambios()
                    conexionDB.cerrar_conexion()
            conexionDB.conectarse()
            consulta = """DELETE FROM etiquetas_eventos 
                        WHERE id_eventos=%s AND id_etiquetas NOT IN (%s)"""
            marcadores = ','.join(['%s'] * len(conjunto_de_id_etiquetas))
            valores = tuple(conjunto_de_id_etiquetas)
            print(valores);
            consulta_final = consulta % (evento.id,marcadores)
            conexionDB.ejecutar_consulta(consulta_final,valores);
            conexionDB.aplicar_cambios()
            conexionDB.cerrar_conexion()    
        except mysql.connector.IntegrityError:
            print("Registro con fecha Duplicada")
            return False
        except mysql.connector.Error as e:
            print(f"Codigo de error numero {e.errno}")
            return False
        finally:
            conexionDB.cerrar_conexion()
        return True

    def etiqueta_relacionada_a_evento(self,conexionDB,evento_id,etiqueta_id):
        try:
            conexionDB.conectarse()
            consulta = """SELECT COUNT(*) FROM 
                        etiquetas_eventos 
                        WHERE id_eventos=%s AND id_etiquetas=%s"""
            conexionDB.ejecutar_consulta(consulta,(evento_id,etiqueta_id))
            registros = conexionDB.obtener_registro()[0]
            print(registros);
        except mysql.connector.DatabaseError:
            print("Ocurrio un error en la base de datos")
        finally:
            conexionDB.cerrar_conexion()
        return registros==0
