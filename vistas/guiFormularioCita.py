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
		cedula = str(self.txtPaciente.text()) # Ontengo la cedula ingresada
		c = dCita() # Instancia de la clase cita
		datos = c.comprobarPaciente(cedula) # Resultado de la consulta obtenida 
		if datos == False: # Si retorna falso, es decir, no existe el paciente
			QtWidgets.QMessageBox.information(self, 'Informacion', 'No existe un paciente con este número de cédula', QtWidgets.QMessageBox.Ok)
		else: # Si el paciente existe muestro su nombre en un campo
			self.txtNombrePaciente.setText(str(datos[0][2])+' '+str(datos[0][3]))


	def registrarCita(self):
		paciente = str(self.txtNombrePaciente.text())
		doctor = str(self.txtDoctor.text())
		descripcion = str(self.txtDescripcion.text())
		fecha = str(self.txtFecha.text())
		hora = str(self.txtHora.text())
		descripcion = str(self.txtDescripcion.text())
		if len(paciente) > 0: # solo si se ha realizado la búsqueda de paciente se registrará la cita
			c = dCita() # Instancia de la clase Cita
			QtWidgets.QMessageBox.information(self, 'Informacion', c.registrarCita(doctor, descripcion, fecha, hora), QtWidgets.QMessageBox.Ok)
		else:
			QtWidgets.QMessageBox.information(self, 'Informacion', 'Seleccione un paciente', QtWidgets.QMessageBox.Ok)
