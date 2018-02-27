from PyQt5 import uic, QtWidgets, QtGui, QtCore, Qt #importamos uic y QtWidgets desde el modulo PyQt5
import sys, os
# Importacion de modulos de  datos
sys.path.append('Datos')
from dCitas import *

qtCita = 'diseno/formularioCita.ui' # Archivo con los componentes gráficos
Ui_Cita, QtBaseClass3 = uic.loadUiType(qtCita)  # carga del archivo

class Cita(QtWidgets.QMainWindow, Ui_Cita):
	def __init__(self, date, hora):
		QtWidgets.QMainWindow.__init__(self)
		Ui_Cita.__init__(self) # Iniciar el diseño de qt creator
		self.setupUi(self)
		self.setWindowTitle("Nueva Cita")
		self.fecha = (str(date.day()) +'/'+str(date.month()) +'/'+str(date.year()))
		self.txtFecha.setDate(datetime.datetime.strptime(self.fecha, "%d/%m/%Y"))
		self.txtHora.setText(hora)
		self.btnBuscarPaciente.clicked.connect(self.comprobarPaciente)
		self.btnGuardar.clicked.connect(self.registrarCita)

	def comprobarPaciente(self):
		cedula = str(self.txtPaciente.text())
		c = dCita()
		datos = c.comprobarPaciente(cedula)
		if datos == False:
			QtWidgets.QMessageBox.information(self, 'Informacion', 'No existe un paciente con este número de cédula', QtWidgets.QMessageBox.Ok)
		else:
			self.txtNombrePaciente.setText(str(datos[0][2])+' '+str(datos[0][3]))


	def registrarCita(self):
		paciente = str(self.txtNombrePaciente.text())
		doctor = str(self.txtDoctor.text())
		descripcion = str(self.txtDescripcion.text())
		fecha = str(self.txtFecha.text())
		hora = str(self.txtHora.text())
		descripcion = str(self.txtDescripcion.text())
		#c = dCita(None, paciente, doctor, descripcion, fecha, hora)
		if len(paciente) > 0:
			c = dCita()
			QtWidgets.QMessageBox.information(self, 'Informacion', c.registrarCita(doctor, descripcion, fecha, hora), QtWidgets.QMessageBox.Ok)
		else:
			QtWidgets.QMessageBox.information(self, 'Informacion', 'Seleccione un paciente', QtWidgets.QMessageBox.Ok)
