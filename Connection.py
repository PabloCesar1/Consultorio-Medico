"""Aplicación de Consultorio Médico.
@authors: P. España B, A. Castillo, F. Bermello.
Creado el 13 de Febrero de 2018
Última Actualización:
"""
import psycopg2 # Módulo para conexión con postgres
import sys # Módulo de sistema

class Connection():
	"""Clase de conexión a la base de datos"""
	def Connect():
		"""Metodo para realizar la conexión"""
		conn = None
		host = 'localhost'
		dbname = 'DB_Empleados'
		user = 'postgres'
		#password = '123456'
		password = '12345'
		connectionString = "host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password) # Cadena de conexión
		try:
			conn = psycopg2.connect(connectionString) # Se realiza la conexión por medio del moóulo psycopg2
		except psycopg2.OperationalError as e:
			#return '¡No se ha podido conectar a la base de datos!\n{0}'.format(e)
			print('No se pudo conectar a la base de datos.\nCerrando aplicacion...')
			sys.exit(1)
		else:
			return conn
	
	c = Connect()
	print(c)
