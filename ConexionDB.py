import mysql.connector

class ConexionDB:
    def __init__(self,base_de_datos="calendario_eventos"):
        self.config = {'user': 'root',
                  'password': 'Mauroo42446109*',
                  'host': 'localhost',
                  'database': base_de_datos}   
    def conectarse(self):
        self.conexion = mysql.connector.connect(**self.config)
        self.cursor = self.conexion.cursor()
    def cerrar_conexion(self):
        self.conexion.close();    
    def ejecutar_consulta(self,consulta,parametros=None):
        self.cursor.execute(consulta,parametros);
    def obtener_registros(self):
        return self.cursor.fetchall()
    def obtener_registro(self):
        return self.cursor.fetchone()