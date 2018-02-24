import sys
import os
sys.path.append('../')
import psycopg2 # Módulo para conexión con postgres
from Connection import Connection # Del directorio Raiz importar el modulo Connection y usar la clase Connection


class Paciente():
	def obtenerPacientes(self):
		"""Método para buscar los empleados de la base de datos y mostrarlos en una tabla"""
		self.conn = Connection.Connect()
		cursor = self.conn.cursor()
		cursor.execute("SELECT * FROM empleado") # Sentencia para consultar en la tabla empleado
		datos = cursor.fetchall() # Obtengo el resultado de la consulta
		cursor.close()
		self.conn.close() # Se realiza un conmit
		return datos