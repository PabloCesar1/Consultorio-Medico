import sys
import os
import psycopg2 
import datetime
sys.path.append('../')
from Connection import Connection

class dCita():

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

    def consultaCitas(self): # Usado para citas por meses
        """Método de consulta de todas la citas médicas"""
        self.conn = Connection.Connect() # Conexión a la base de datos
        cursor = self.conn.cursor() # Creación del cursor
        cursor.execute("SELECT * FROM citas") # Sentencia para consulta
        result = cursor.fetchall() # Obteniendo resultados
        cursor.close()
        self.conn.close()
        return result # resultado

    def consultaCitasPorDias(self, fechaEspecificada): # Usado para citas por meses
        """Método de consulta de todas la citas médicas"""
        self.conn = Connection.Connect() # Conexión a la base de datos
        cursor = self.conn.cursor() # Creación del cursor
        fecha = (str(fechaEspecificada.day()) +'/'+str(fechaEspecificada.month()) +'/'+str(fechaEspecificada.year()))
        cursor.execute("SELECT * FROM citas WHERE fecha =  %s;", [fecha])
        result = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return result # resultado

    def numeroCitasDiarias(self):
        """Método para consultar las citas médicas del día actual"""
        self.conn = Connection.Connect() # Conexion a la base de datos
        cursor = self.conn.cursor() # Creacion de cursor
        d = datetime.datetime.now() # Fecha de hoy en formato YYYY-DD-MM HH:MM:SS
        hoy = (str(d.day)+'/'+str(d.month)+'/'+str(d.year)) # Variable con fecha en formato dd/m/yyyy
        cursor.execute("SELECT * FROM citas WHERE fecha =  %s;", [hoy]) # Consultar citas con la fecha de hoy
        result = cursor.fetchall() # resultado de la consulta
        cursor.close()
        self.conn.close()
        return [result, hoy] # retorno el resultado de la consulta y a su vez la fecha actual

#c = dCita()
#print(c.consultaCitasPorDias(datetime.datetime.now()))