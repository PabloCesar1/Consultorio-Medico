import sys
import os
import psycopg2 
from Connection import Connection

class dCita():
    """Clase para acceder a los datos"""
    # Referencia a los campos de la tabla 'Citas'
    # Variables De tipo privado
    def __init__(self, idcita=None, paciente=None, doctor=None, descripcion=None, fecha=None, hora=None):
        self.idCita = idcita
        self.paciente = paciente
        self.doctor = doctor
        self.descripcion = descripcion
        self.fecha = fecha
        self.hora = hora

    def registrarCita(self):
        """Metodos con las operaciones de registro de una cita"""
        self.conn = Connection.Connect() # Conexión a la base de datos
        cursor = self.conn.cursor() # Creación del cursor
        mensaje = ''
        # Ejecución de la sentencia para insertar en la tabla citas
        cursor.execute("INSERT INTO citas (paciente, doctor, descripcion, fecha, hora) VALUES (%s, %s, %s, %s, %s);",
         [self.paciente, self.doctor, self.descripcion, self.fecha, self.hora])
        mensaje = 'Registro Correcto'
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return mensaje

    def consultaCitas(self):
        """Método de consulta de todas la citas médicas"""
        self.conn = Connection.Connect() # Conexión a la base de datos
        cursor = self.conn.cursor() # Creación del cursor
        cursor.execute("SELECT * FROM citas") # Sentencia para consulta
        result = cursor.fetchall() # Obteniendo resultados
        cursor.close()
        self.conn.close()
        return result # resultado

