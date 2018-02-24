import sys
import os
import psycopg2 # Módulo para conexión con postgres
from Connection import Connection # Del directorio Raiz importar el modulo Connection y usar la clase Connection


class Paciente(object):
	def __init__(self,id,cedula,nombres,apellidos,fecha,edad,aportaciones,dir1,dir2,telf1,telf2,email,sueldo,diasLabor,sexo,nivelAcad,cuentaBamc,tipoDisc,nombreRec,telfRec,celRec,ciudad,foto):
		self.id = id
		self.cedula = cedula
		self.nombres = nombres
		self.apellidos = apellidos 
		self.fecha = fecha
		self.edad = edad
		self.aportaciones = aportaciones
		self.dir1 = dir1
		self.dir2 = dir2
		self.telf1 = telf1
		self.telf2 = telf2
		self.email = email
		self.sueldo = sueldo
		self.diasLabor = diasLabor
		self.sexo = sexo
		self.nivelAcad = nivelAcad
		self.cuentaBamc = cuentaBamc
		self.tipoDisc = tipoDisc
		self.nombreRec = nombreRec
		self.telfRec = telfRec
		self.celRec = celRec
		self.ciudad = ciudad
		self.foto = foto

	def RegistrarPaciente(self):
		mensaje = ""
		if self.verificar(self.cedula):
			self.conn = Connection.Connect()
			cursor = self.conn.cursor()
			cursor.execute("INSERT INTO empleado (cedula, nombres, apellidos, fecha_nacimiento, edad, numero_aportaciones, direccion1,"
				"direccion2, telefono1, telefono2, email, sueldo, dias_laborales, genero, nivel_academico, numero_cuenta_bancaria, tipo_discapacidad,"
				"nombre_recomendado, telefono_recomendado, celular_recomendado, ciudad, foto)"
				" VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s , %s, %s, %s, %s);", 
				[self.cedula, self.nombres, self.apellidos, self.fecha, self.edad, self.aportaciones, self.dir1, self.dir2,  self.telf1, 
				self.telf2, self.email, self.sueldo, self.diasLabor, self.sexo, self.nivelAcad, self.cuentaBamc, self.tipoDisc,
				self.nombreRec, self.telfRec, self.celRec, self.ciudad, 'Ninguna'])
			mensaje = 'Registro Correcto'
			self.conn.commit()
			cursor.close()
			self.conn.close()
		else:
			mensaje = "Cedula Incorrecta"
		return mensaje

	def verificar(self, nro):
		self.mensaje = ''
		l = len(nro)
		if l == 10 or l == 13: # verificar la longitud correcta
			cp = int(nro[0:2])
			if cp >= 1 and cp <= 22: # verificar codigo de provincia
				tercer_dig = int(nro[2])
				if tercer_dig >= 0 and tercer_dig < 6 : # numeros enter 0 y 6
					if l == 10:
						return self.validar_ced_ruc(nro,0)     
					elif l == 13:
						return self.validar_ced_ruc(nro,0) and nro[10:13] != '000' # se verifica q los ultimos numeros no sean 000
				elif tercer_dig == 6:
					return self.validar_ced_ruc(nro,1) # sociedades publicas
				elif tercer_dig == 9: # si es ruc
					return self.validar_ced_ruc(nro,2) # sociedades privadas
				else:
					return False
			else:
				return False
		else:
			return False
					
	def validar_ced_ruc(self, nro, tipo):
		total = 0
		if tipo == 0: # cedula y r.u.c persona natural
			base = 10
			d_ver = int(nro[9])# digito verificador
			multip = (2, 1, 2, 1, 2, 1, 2, 1, 2)
		elif tipo == 1: # r.u.c. publicos
			base = 11
			d_ver = int(nro[8])
			multip = (3, 2, 7, 6, 5, 4, 3, 2 )
		elif tipo == 2: # r.u.c. juridicos y extranjeros sin cedula
			base = 11
			d_ver = int(nro[9])
			multip = (4, 3, 2, 7, 6, 5, 4, 3, 2)
		for i in range(0,len(multip)):
			p = int(nro[i]) * multip[i]
			if tipo == 0:
				total+=p if p < 10 else int(str(p)[0])+int(str(p)[1])
			else:
				total+=p
		mod = total % base
		val = base - mod if mod != 0 else 0
		return val == d_ver